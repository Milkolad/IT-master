namespace Achivement_2.Models
{
    public interface INumberstoreDatabaseSettings
    {
        string NumbersCollectionName { get; set; }
        string ConnectionString { get; set; }
        string DatabaseName { get; set; }
    }
}