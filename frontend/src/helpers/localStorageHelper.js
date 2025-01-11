function addToLocalStorage(key, value) {
    if (typeof key !== 'string') {
      console.error('Key must be a string.');
      return;
    }
    localStorage.setItem(key, JSON.stringify(value));
  }

  function getFromLocalStorage(key) {
    if (typeof key !== 'string') {
      console.error('Key must be a string.');
      return null;
    }
    const value = localStorage.getItem(key);
    return value ? JSON.parse(value) : null;
  }

  function clearLocalStorage() {
    localStorage.clear();
  }
  
  export { addToLocalStorage, getFromLocalStorage, clearLocalStorage };