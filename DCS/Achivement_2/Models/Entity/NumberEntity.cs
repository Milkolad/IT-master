using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;

namespace Achivement_2.Models
{
    public class NumberEntity
    {
        [BsonId]
        [BsonRepresentation(BsonType.ObjectId)]
        public string Id { get; set; }

        [BsonElement("number")]
        public int Number { get; set; }
    }
}