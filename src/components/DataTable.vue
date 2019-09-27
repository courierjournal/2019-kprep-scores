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
      <tbody>
        <DataRow v-for="(item,index) in data" :key="index" :rowData="item" />
      </tbody>
    </table>
  </div>
</template>

<script>
import DataRow from "./DataRow";

export default {
  name: "DataTable",
  components: { DataRow },
  props: ["data"]
};
</script>

<style>
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

tbody> tr:nth-child(even){
    background-color:#eee;
}

th:first-child {
  text-align: left;
}

th:nth-child(2) {
  text-align: left;
}

th:nth-child(3) {
  text-align: center;
}

th:last-child {
  text-align: center;
}


</style>