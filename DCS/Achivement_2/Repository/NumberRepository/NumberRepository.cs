using System.Collections.Generic;
using System.Linq;
using Achivement_2.Models;
using MongoDB.Driver;
using Newtonsoft.Json;

namespace Achivement_2.Repository
{
    public class NumberRepository : INumberRepository
    {
        private readonly StorageContext _context;
        private readonly string _collection;
        public NumberRepository(StorageContext context, string collection)
        {
            _context = context;
            _collection = collection;
        }
        public NumberEntity Add(NumberEntity item)
        {
            NumberEntity result = null;

            long oldListLength = _context.Base.ListLength(_collection);

            if (_context.Base != null)
            {
                long newListLength = _context.Base.ListRightPush(_collection, JsonConvert.SerializeObject(item));
                if (newListLength > oldListLength) 
                {
                    result = Get().ToList().Find(x => x.Number == item.Number);
                }
            }

            return result;
        }

        public bool Delete(NumberEntity item)
        {
            bool result = false;
            List<NumberEntity> numbers = Get().ToList();

            NumberEntity number = numbers.Find(x => x.Number == item.Number);

            if (_context.Base != null)
            {
                long removed = _context.Base.ListRemove(_collection, JsonConvert.SerializeObject(numbers));

                if (removed > 0)
                {
                    result = true;
                }
            }
            return result;
        }

        public IEnumerable<NumberEntity> Get()
        {
            List<NumberEntity> result = null;
            result = _context.Base.ListRange(_collection, start: 0, stop: -1).ToList().Select(x => JsonConvert.DeserializeObject<NumberEntity>(x.ToString())).ToList();
            return result;
        }

    }
}