using System;
using Achivement_2.Models;
using StackExchange.Redis;

namespace Achivement_2
{
    public class StorageContext
    {
        private readonly Lazy<ConnectionMultiplexer> _connection;

        public IDatabase Base { get; set; }

        public StorageContext(RedisCache cacheConnection)
        {
            _connection = new Lazy<ConnectionMultiplexer>(() => ConnectionMultiplexer.Connect(cacheConnection.Configuration)); 

            Base = _connection.Value.GetDatabase();
        }
    }
}