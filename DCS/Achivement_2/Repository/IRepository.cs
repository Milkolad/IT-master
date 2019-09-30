using System.Collections.Generic;

namespace Achivement_2.Repository
{
    public interface IRepository<T>
    {
        T Add(T item);
        IEnumerable<T> Get();
        bool Delete(T item);
    }
}