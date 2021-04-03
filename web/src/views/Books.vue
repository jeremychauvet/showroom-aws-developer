<template>
  <div class="books">
    <h1>Books</h1>

    <div class="row row-cols-1 row-cols-md-2 g-4">
      <div class="col" v-for="book in books" :key="book.message">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">{{ book.BookTitle }}</h5>
            <h6 class="card-subtitle mb-2 text-muted">{{ book.BookAuthor }}</h6>
            <p class="card-text">Stock : {{ book.BookStock }} - ISBN : {{ book.ISBN }}</p>
            <a href="#" class="card-link">Click to buy this book</a>
          </div>
        </div>
      </div>

      <div class="card mb-3" style="max-width: 540px;">
        <div class="row g-0">
          <div class="col-md-4">
            <img src="@/assets/book.jpg" alt="Book" class="cover">
          </div>
          <div class="col-md-8">
            <div class="card-body">
              <h5 class="card-title">Card title</h5>
              <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
              <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
            </div>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import { api } from '../api';

export default {
  name: 'Books',
  data () {
    return {
      books: null,
      error: null
    }
  },
  mounted () {
    api.get('https://xxxxxxxxx.execute-api.eu-central-1.amazonaws.com/stage/book/display')
    .then(response => {
      this.books = response.data
    })
    .catch(e => {
      this.error = e
    })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

img.cover {
  width: 100%;
  height: 100%;
  margin: 0 12px 0 -12px;
}
</style>
