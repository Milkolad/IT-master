using System;
using Achivement_2.Models;
using StackExchange.Redis;

namespace Achivement_2
{
    public class StorageContext
    {
        private readonly ConnectionMultiplexer _connection;

        public IDatabase Base { get; set; }

        public StorageContext(RedisCache cacheConnection)
        {
            _connection = ConnectionMultiplexer.Connect(cacheConnection.Configuration); 

            Base = _connection.GetDatabase();
        }
    }
}