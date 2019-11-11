using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using Achivement_2.Models;
using Achivement_2.Repository;
using Microsoft.AspNetCore.Mvc;
using Newtonsoft;
using Newtonsoft.Json;

namespace Achivement_2.Controllers
{
    [ApiController]
    [Route("increment")]
    public class ValueController : ControllerBase
    {
        private readonly IRepository<NumberEntity> _repository;
        public ValueController(IRepository<NumberEntity> repository)
        {
            _repository = repository;
        }

        [HttpGet]
        public IActionResult Get()
        {
            IActionResult result = null;
            IEnumerable<NumberEntity> array;
            try {
                array = _repository.Get();
                result = Ok(array);
            } catch (Exception e)
            {
                result = NotFound(e);
            }
            
            return result;
        }

        [HttpPost]
        public IActionResult Post([FromBody]NumberEntity item)
        {
            IActionResult result = null;
            try {
                var numbers = _repository.Get().OrderBy(x => x.Number).ToList();
                NumberEntity number = numbers.LastOrDefault();
                if (number != default(NumberEntity) && number.Number == item.Number)
                {
                    ExceptionResult exp = new ExceptionResult()
                    {
                        Error = "Exception 1: number is already added",
                        Type = "1"
                    };
                    result = BadRequest(exp);
                } else if (number != default(NumberEntity) && number.Number > item.Number)
                {
                    ExceptionResult exp = new ExceptionResult()
                    {
                        Error = "Exception 2: number is less than added",
                        Type = "2"
                    };
                    result = BadRequest(exp);
                } else 
                {
                    NumberEntity new_number = _repository.Add(item);
                    Models.OkResult ok = new Models.OkResult()
                    {
                        Result =  new_number.Number + 1
                    };
                    result = Ok(ok);
                }
            } catch (Exception e)
            {
                result = NotFound(e);
            }
            
            return result;
        }
    }
}