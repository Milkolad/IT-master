using Newtonsoft.Json;

namespace Achivement_2.Models
{
    public class ExceptionResult
    {
        [JsonProperty("error")]
        public string Error { get; set; }

        [JsonProperty("type")]
        public string Type { get; set; }
    }
}