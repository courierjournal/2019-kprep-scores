<template>
  <div class="table-container">
    <div class="table">
      <div class="thead">
        <div class="tr">
          <div class="th">School</div>
          <div class="th">Designation</div>
          <div class="th">Stars</div>
          <div class="th">More</div>
        </div>
      </div>
      <div class="tbody">
        <DataRow v-for="(item,index) in data" :rowData="item" :key="index" />
      </div>
    </div>
  </div>
</template>

<script scoped>
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

.table {
  display: table;
  width: 100%;
  border-collapse: collapse;
}

.thead {
  display: table-header-group;
}

.tbody {
  display: table-row-group;
}

.tr {
  display: table-row;
}

.td,
.th {
  display: table-cell;
  vertical-align:middle;
  padding:1em;
}

.thead > .tr {
  border-bottom: 1px solid #ccc;
}

.th {
  font-weight:bold;
}

.tbody > .tr:nth-child(even) {
  background-color: #eee;
}

.th:first-child, .td:first-child  {
  text-align: left;
}

.th:nth-child(2), .td:nth-child(2) {
  text-align: left;
}

.th:nth-child(3), .td:nth-child(3) {
  text-align: center;
}

.th:last-child, .td:last-child  {
  text-align: center;
}
</style>