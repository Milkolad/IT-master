using Newtonsoft.Json;

namespace Achivement_2.Models
{
    public class OkResult
    {
        [JsonProperty("result")]
        public int Result { get; set; }
    }
}