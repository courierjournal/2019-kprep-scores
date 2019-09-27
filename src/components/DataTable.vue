<template>
  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>School</th>
          <th>Designation</th>
          <th>Stars</th>
          <th>More</th>
        </tr>
      </thead>
    </table>
  </div>
</template>

<script>
export default {
  name: "DataTable"
};
</script>

<style scoped>
.table-container {
  padding: 1em;
}

table {
  width: 100%;
  border-collapse: collapse;
}

thead > tr {
  border-bottom: 1px solid #ccc;
}

thead > tr > th {
  padding: 1em;
}
</style>