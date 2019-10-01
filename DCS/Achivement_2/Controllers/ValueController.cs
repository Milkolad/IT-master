using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;

namespace Achivement_2.Controllers
{
    [ApiController]
    [Route("api/values")]
    public class ValueController : ControllerBase
    {
        public ValueController()
        {

        }

        public async Task<ActionResult<string>> GetTask()
        {
            string result = "";

            return new ActionResult<string>(result);
        }
    }
}