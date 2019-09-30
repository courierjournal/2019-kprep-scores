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
/*
NOTE: why are we using our own styles here to essentially generate a table?
Because as of this version of Vue, templates must have exactly one root element.
This causes a problem when trying to create an iterable component of a table that should have 2 <tr>
elements for every row of data (one main and one collapsible). https://github.com/vuejs/vue/issues/7088#issuecomment-357899727
There are numerous 'hacks' for this but at this point it was decided to just create a psuedo
table out of divs. If vue ever supports Fragments ala React, refactor this all back into a table.
*/
.table-container {
  padding: 1em;
  min-height:70vh;
  overflow:hidden;
}

.tr{
    display:flex;
}

.td,
.th {
  padding:1em;
}

.thead > .tr {
  border-bottom: 1px solid #ccc;
  font-family: "Unify Sans", sans-serif;
}

.th {
  font-weight:bold;
}

.tbody > .tr:nth-child(even) {
  background-color: #eee;
}

.th:first-child, .td:first-child  {
  text-align: left;
  width:40%;
}

.th:nth-child(2), .td:nth-child(2) {
  text-align: left;
  width:25%
}

.th:nth-child(3), .td:nth-child(3) {
  text-align: center;
  width:25%;
}

.th:last-child, .td:last-child  {
  text-align: center;
  width:10%;
}
</style>