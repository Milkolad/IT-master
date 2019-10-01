namespace Achivement_2.Models
{
    public class NumberstoreDatabaseSettings : INumberstoreDatabaseSettings
    {
        public string NumbersCollectionName { get; set; }
        public string ConnectionString { get; set; }
        public string DatabaseName { get; set; }
    }
}