<template>
  <div class="home">
    <div class="jumbotron">
      <h1 class="display-4">Find the perfect book.</h1>
      <p class="lead">In this digital world, find the perfect book is difficult as never. Find it here. Book your book.</p>
    </div>

    <div class="container">
      <h2>Latest books added</h2>

      <div class="row">

        <div class="col-md-4 mb-4">
          <div class="card">
            <img class="card-img-top" src="@/assets/books/hosea.png" alt="Card image cap">
            <div class="card-body">
              <h5 class="card-title">Hosea</h5>
              <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
            </div>
            <div class="card-footer">
              <small class="text-muted">3 books in stock.</small>
            </div>
          </div>
        </div>

        <div class="col-md-4 mb-4">
          <div class="card">
            <img class="card-img-top" src="@/assets/books/isaiah.png" alt="Card image cap">
            <div class="card-body">
              <h5 class="card-title">Isaiah</h5>
              <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
            </div>
            <div class="card-footer">
              <small class="text-muted">3 books in stock.</small>
            </div>
          </div>
        </div>

         <div class="col-md-4 mb-4">
          <div class="card">
            <img class="card-img-top" src="@/assets/books/hosea.png" alt="Card image cap">
            <div class="card-body">
              <h5 class="card-title">Hosea</h5>
              <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
            </div>
            <div class="card-footer">
              <small class="text-muted">3 books in stock.</small>
            </div>
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
}

.card {
  border: none;
}
</style>
