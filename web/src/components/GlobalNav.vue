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
                <i class="gg-user"></i>
              </li>
              <li class="nav-item">
                <i class="gg-box"></i>
              </li>
          </ul>
      </div>
    </nav>
    <nav class="navbar navbar-expand-lg sub-navbar">
      <router-link class="nav-link" to="/">Home</router-link>
      <router-link class="nav-link" to="/books">Books</router-link>
      <router-link class="nav-link" to="#">About</router-link>
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

.navbar-brand-custom:hover {
  color: #D95B43;
}

.navbar {
  padding: 1rem 0 .7rem 0 !important;
}

.sub-navbar {
  justify-content: center !important;
  border-top: 1px solid #E5E5E5;
}

.sub-navbar > a {
  color: #8E8E8E;
  font-family: 'Oswald', sans-serif;
  font-weight: 200 !important;
  font-size: 1.1rem;
  padding: 0 2rem;
  text-transform: uppercase;
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

.navbar-nav > .nav-item {
  margin: 0 0 0 2rem;
  color: #8E8E8E;
}

.navbar-nav > .nav-item:hover {
  color: #212121;
  cursor: pointer;
}

</style>
