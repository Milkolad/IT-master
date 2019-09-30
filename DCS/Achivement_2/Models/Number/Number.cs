using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;

namespace Achivement_2.Models
{
    public class Number
    {
        [BsonId]
        [BsonRepresentation(BsonType.ObjectId)]
        public string Id { get; set; }

        [BsonElement("Value")]
        public int Value { get; set; }
    }
}