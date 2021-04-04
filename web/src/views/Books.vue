<template>
  <div class="books">
    <h1>Books</h1>

    <div class="alert alert-danger" role="alert" v-if="books === null && error != null">
      No books available.
    </div>
    <div class="row row-cols-1 row-cols-md-2 g-4" v-else>
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
    api.get('/book/display')
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
