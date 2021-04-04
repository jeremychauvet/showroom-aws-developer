<template>
  <div class="home">
    <div class="jumbotron">
      <h1 class="display-4">Find the perfect book.</h1>
      <p class="lead">In this digital world, find the perfect book is difficult as never. Find it here. Book your book.</p>
    </div>

    <div class="latest-books">
      <h2>Latest books added</h2>

      <div class="card-deck">
        <div class="card">
          <img class="card-img-top" src="@/assets/books/sincerely-media-_f3VOwm2YWg-unsplash.jpg" alt="Card image cap">
          <div class="card-body">
            <h5 class="card-title">Issiah</h5>
            <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
          </div>
          <div class="card-footer">
            <small class="text-muted">3 books in stock.</small>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home'
}
</script>

<style>
.jumbotron {
  margin: 5rem 0;
  padding: 2rem 0;
  text-align: center;
  color: #404040;
  background-image: url("../assets/hero.jpg");
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  height: 40rem;
}

.card {
  max-width: 22rem;
}
</style>
