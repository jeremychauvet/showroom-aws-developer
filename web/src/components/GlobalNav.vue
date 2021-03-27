<template>
  <div class="GlobalNav">
    <nav class="navbar navbar-expand-md">
      <div class="container-fluid">
          <a class="navbar-brand" href="#">
            <img src="@/assets/logo.png" alt="" width="35" height="35">
          </a>
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
      </div>
  </nav>

  </div>
</template>

<script>
export default {
  name: "GlobalNav"
};
</script>
