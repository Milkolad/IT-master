using System.Linq;
using System.Net;
using System.Net.Http;
using System.Threading.Tasks;
using Achivement_2.Models;
using Achivement_2.Repository;
using Microsoft.AspNetCore.Mvc;
using Newtonsoft;
using Newtonsoft.Json;

namespace Achivement_2.Controllers
{
    [ApiController]
    [Route("/increment")]
    public class ValueController : ControllerBase
    {
        private readonly IRepository<Number> _repository;
        public ValueController(IRepository<Number> repository)
        {
            _repository = repository;
        }

        [HttpGet]
        public ActionResult<HttpResponseMessage> Get()
        {
            HttpResponseMessage result = new HttpResponseMessage();
            result.Content = new StringContent(JsonConvert.SerializeObject(_repository.Get()));
            return result;
        }

        [HttpPost]
        public ActionResult<HttpResponseMessage> Post([FromBody]Number item)
        {
            HttpResponseMessage result = new HttpResponseMessage();
            var numbers = _repository.Get().ToList();
            Number number = numbers.Last();
            if (numbers.Count == 0 || number == default(Number))
            {
                Number new_number = _repository.Add(item);
                result.Content = new StringContent((new_number.Value + 1).ToString());
                result.ReasonPhrase = "OK";
                result.StatusCode = HttpStatusCode.OK;
            } else if (number.Value == item.Value)
            {
                result.ReasonPhrase = "Exception 1: number is already added";
                result.StatusCode = HttpStatusCode.BadRequest;
            } else if (number.Value > item.Value)
            {
                result.ReasonPhrase = "Exception 2: number is less than added";
                result.StatusCode = HttpStatusCode.BadRequest;
            }
            return result;
        }
    }
}