using System.Linq;
using System.Threading.Tasks;
using Achivement_2.Models;
using Achivement_2.Repository;
using Microsoft.AspNetCore.Mvc;
using Newtonsoft;
using Newtonsoft.Json;

namespace Achivement_2.Controllers
{
    [ApiController]
    [Route("api/values")]
    public class ValueController : ControllerBase
    {
        private readonly IRepository<Number> _repository;
        public ValueController(IRepository<Number> repository)
        {
            _repository = repository;
        }

        [HttpGet]
        public ActionResult<string> Get()
        {
            string result = "";
            result = JsonConvert.SerializeObject(_repository.Get());
            return new ActionResult<string>(result);
        }

        [HttpPost]
        public ActionResult<string> Post([FromBody]Number item)
        {
            string result = "";
            var numbers = _repository.Get().ToList();
            Number number = numbers.Find(x => x.Value == item.Value);
            if (numbers.Count == 0 || number == default(Number))
            {
                Number new_number = _repository.Add(item);
                result = (new_number.Value + 1).ToString();
            } else if (number.Value == item.Value)
            {
                result = "Exception 1: number is already added";
            } else if (number.Value > item.Value)
            {
                result = "Exception 2: number is less than added";
            }
            return new ActionResult<string>(result);
        }
    }
}