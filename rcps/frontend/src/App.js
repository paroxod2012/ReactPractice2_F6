import './App.css';
import {useState, useEffect} from 'react';

function App() {

  const [categories, setCategories] = useState([])
  const [category, setCategory] = useState(null)
  useEffect( () => {
    fetch('http://127.0.0.1:8000/api/categories/?format=json')
    .then((response) => response.json())
    .then((data) => {
      setCategories([{'id':null,'title': null}].concat(data));
    })
    .catch((err) => {
      console.log(err.message);
    });
  }, []);

  const [recipe, setRecipe] = useState([]);
  useEffect( () => {
    let url = 'http://127.0.0.1:8000/api/recipes/?format=json'
    if (category) {
        url += '&category=' + category
    }
    fetch(url)
    .then((response) => response.json())
    .then((data) => {
      console.log(data)
      setRecipe(data);
    })
    .catch((err) => {
      console.log(err.message);
    });
  }, [category])

  return (
    <div className="App">
      <header className="App-header">
        <h2>Cookbook</h2>
        <div>
          {recipe.map((r) => {
            return <div key={r.id}>
            <div>{r.name} : {r.description}</div>
            <hr/>
            <div>{r.image ? <img src={r.image} alt=""/> : ''}</div>
            </div>
          })}
        </div>
        <h2>Category choice</h2>
          <div>
          {categories.map((c) => {
            return <div key={c.id} onClick={() => setCategory(c.id)}>{c.title}</div>
          })}
        </div>
      </header>
    </div>
  );


}

export default App;
