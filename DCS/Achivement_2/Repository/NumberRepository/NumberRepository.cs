using System.Collections.Generic;
using Achivement_2.Models;
using MongoDB.Driver;

namespace Achivement_2.Repository
{
    public class NumberRepository : INumberRepository
    {
        private readonly MongoClient _client;
        private readonly IMongoDatabase _dataBase;
        private readonly IMongoCollection<NumberEntity> _numbers;
        public NumberRepository(INumberstoreDatabaseSettings settings)
        {
            _client = new MongoClient(settings.ConnectionString);
            _dataBase = _client.GetDatabase(settings.DatabaseName);
            _numbers = _dataBase.GetCollection<NumberEntity>(settings.NumbersCollectionName);
        }
        public NumberEntity Add(NumberEntity item)
        {
            NumberEntity result = null;
            _numbers.InsertOne(item);
            result = _numbers.Find(number => number.Number == item.Number).FirstOrDefault();
            return result;
        }

        public bool Delete(NumberEntity item)
        {
            DeleteResult result = _numbers.DeleteOne(number => number.Id == item.Id);
            return result.IsAcknowledged;
        }

        public IEnumerable<NumberEntity> Get()
        {
            List<NumberEntity> result = null;
            result = _numbers.Find(number => number is NumberEntity).ToList();
            return result;
        } 
    }
}