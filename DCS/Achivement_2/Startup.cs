using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Achivement_2.Models;
using Achivement_2.Repository;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Options;

namespace Achivement_2
{
    public class Startup
    {
         public Startup(IHostingEnvironment env)
        {
            var builder = new ConfigurationBuilder()
                .SetBasePath(env.ContentRootPath)
                .AddJsonFile("appsettings.json", optional: true, reloadOnChange: true)
                .AddJsonFile($"appsettings.{env.EnvironmentName}.json", optional: true)
                .AddEnvironmentVariables();

            Configuration = builder.Build();
            Console.WriteLine(Configuration.GetSection("APP_PORT").Value);
        }

        public IConfiguration Configuration { get; }

        public void ConfigureServices(IServiceCollection services)
        {
            services.AddMvc().SetCompatibilityVersion(CompatibilityVersion.Version_2_1);
            
            services.AddSingleton<RedisCache>(sp =>
            {
                return new RedisCache() 
                    { 
                        Configuration = Configuration.GetSection("DB_HOST").Value + 
                        ":" + 
                        Configuration.GetSection("DB_PORT").Value + 
                        ",abortConnect=False,resolveDns=True"
                    };
            });

            services.AddSingleton<StorageContext>(sp => 
            {
                return new StorageContext(sp.GetRequiredService<RedisCache>());
            });

            services.AddTransient<IRepository<NumberEntity>, NumberRepository>(sp =>
            {
                return new NumberRepository(sp.GetRequiredService<StorageContext>(), Environment.GetEnvironmentVariable("DB_NAME"));
            });
            
        }

        public void Configure(IApplicationBuilder app, IHostingEnvironment env)
        {
            app.UseDeveloperExceptionPage();
            app.UseMvc();
        }
    }
}
