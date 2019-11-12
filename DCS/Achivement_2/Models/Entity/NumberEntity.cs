using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;
using Newtonsoft.Json;

namespace Achivement_2.Models
{
    public class NumberEntity
    {
        [BsonId]
        [BsonRepresentation(BsonType.ObjectId)]
        [JsonProperty("_id")]
        public string Id { get; set; }

        [BsonElement("number")]
        [JsonProperty("number")]
        public int Number { get; set; }
    }
}