using System.Collections.Generic;
using Achivement_2.Models;
using MongoDB.Driver;

namespace Achivement_2.Repository
{
    public class NumberRepository : INumberRepository
    {
        private readonly MongoClient _client;
        private readonly IMongoDatabase _dataBase;
        private readonly IMongoCollection<Number> _numbers;
        public NumberRepository(INumberstoreDatabaseSettings settings)
        {
            _client = new MongoClient(settings.ConnectionString);
            _dataBase = _client.GetDatabase(settings.DatabaseName);
            _numbers = _dataBase.GetCollection<Number>(settings.NumbersCollectionName);
        }
        public Number Add(Number item)
        {
            Number result = null;
            _numbers.InsertOne(item);
            result = _numbers.Find(number => number.Value == item.Value).FirstOrDefault();
            return result;
        }

        public bool Delete(Number item)
        {
            DeleteResult result = _numbers.DeleteOne(number => number.Id == item.Id);
            return result.IsAcknowledged;
        }

        public IEnumerable<Number> Get()
        {
            List<Number> result = null;
            result = _numbers.Find(number => number is Number).ToList();
            return result;
        } 
    }
}