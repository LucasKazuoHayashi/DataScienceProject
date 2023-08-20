using BitcoinProject.Configuration;
using BitcoinProject.Controller;
using BitcoinProject.Interfaces;
using BitcoinProject.Services;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Options;
using System;
using System.IO;
using System.ServiceProcess;

namespace BitcoinProjectUpdate
{
    internal static class Program
    {
        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        static void Main()
        {
            //IConfigurationRoot configuration = _InitConfiguration();
            //if (configuration == null) return;

            //var serviceCollection = new ServiceCollection();
            //serviceCollection.ConfigureBitcoinProject(configuration);
            //ServiceProvider serviceProvider = serviceCollection.BuildServiceProvider();

            //var bitcoinProject = serviceProvider.GetService<IBitcoinProjectService>();

            //bitcoinProject.Execute();

            ServiceBase[] ServicesToRun;
            ServicesToRun = new ServiceBase[]
            {
                new BitcoinUpdateDatabase(
                    //CreateServiceProvider().GetRequiredService<IBitcoinOptions>(),
                    //CreateServiceProvider().GetRequiredService<IDatabaseOptions>(),
                    //CreateServiceProvider().GetRequiredService<IBitcoinProjectService>(),
                    //CreateServiceProvider().GetRequiredService<IConnectDatabaseService>()
                    //CreateServiceProvider().GetRequiredService<IQueryBitcoinDataService>()
                    )
            };
            ServiceBase.Run(ServicesToRun);
        }

        private static IConfigurationRoot _InitConfiguration()
        {
            var aqui = Directory.GetCurrentDirectory();

            if (!File.Exists("appsettings.json"))
            {
                Console.WriteLine($"Arquivo de Configuração \"appsettings.json\" não localizado!");
                return null;
            }

            var configuration = new ConfigurationBuilder()
                .SetBasePath(Directory.GetCurrentDirectory())
                .AddJsonFile("appsettings.json", optional: true, reloadOnChange: true)
                .Build();

            return configuration;
        }

        private static IServiceProvider CreateServiceProvider()
        {

            IConfiguration configuration = new ConfigurationBuilder()
                .SetBasePath(Directory.GetCurrentDirectory())
                .AddJsonFile("appsettings.json", optional: false, reloadOnChange: true)
                .Build();

            return new ServiceCollection()
                .Configure<BitcoinOptions>(configuration.GetSection("BitcoinManagerApi"))
                .Configure<DatabaseOptions>(configuration.GetSection("Database"))
                .AddOptions()

                .AddSingleton<BitcoinOptions>()
                .AddSingleton<DatabaseOptions>()
                .AddSingleton<IBitcoinProjectService, BitcoinProjectService>()
                .AddSingleton<IConnectDatabaseService, ConnectDatabaseService>()
                .AddSingleton<IQueryBitcoinDataService, QueryBitcoinDataService>()
                .AddSingleton<IBitcoinOptions>(sp => sp.GetRequiredService<IOptions<BitcoinOptions>>().Value)
                .AddSingleton<IDatabaseOptions>(sp => sp.GetRequiredService<IOptions<DatabaseOptions>>().Value)
                .BuildServiceProvider();
        }
    }
}
