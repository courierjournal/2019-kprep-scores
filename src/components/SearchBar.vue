<template>
  <div class="search-container">
    <input class="search" type="text" placeholder="Enter school or district name" />
  </div>
</template>

<script>
export default {
  name: "SearchBar"
};
</script>

<style scoped>
.search-container {
  text-align: center;
  padding: 2em;
}
.search {
  max-width: 300px;
  width: 100%;
  padding: .3em;
  border:none;
  border-bottom:1px solid #aaa;
  outline:none;
}
</style>