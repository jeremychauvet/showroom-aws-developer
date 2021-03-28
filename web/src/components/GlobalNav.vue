<template>
  <div class="globalnav">
    <nav class="navbar navbar-expand-md">
      <a class="navbar-brand-custom" href="#">MyOnlineBookStore</a>
      <button class="navbar-toggler ms-auto" type="button" data-bs-toggle="collapse" data-bs-target="#collapseNavbar">
          <span class="navbar-toggler-icon"></span>
      </button>
      <div class="navbar-collapse collapse" id="collapseNavbar">
          <ul class="navbar-nav ms-auto">
              <li class="nav-item">
                  <router-link class="nav-link" to="/">Home</router-link>
              </li>
              <li class="nav-item">
                  <router-link class="nav-link" to="/books">Books</router-link>
              </li>
          </ul>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  name: "GlobalNav"
};
</script>

<style>
.globalnav {
  margin-bottom: 45px;
}

.navbar-brand-custom {
  font-family: 'Amatic SC', cursive !important;
  text-decoration: none;
  color: #D95B43;
  font-size: 25px;
  letter-spacing: 2px;
}

.nav-link {
  color: #636363;
  font-weight: 500;
  font-size: 19px;
  font-weight: 700 !important;
  font-family: 'Roboto', sans-serif;
}

.nav-link:hover {
  color: #212121;
}
</style>
