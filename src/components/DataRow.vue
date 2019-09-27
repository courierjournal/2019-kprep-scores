<template>
  <tr>
    <td>{{rowData.n}}</td>
    <td></td>
    <td>{{rowData.s}}★</td>
    <td></td>
  </tr>
</template>

<script>
export default {
  name: "DataRow",
  props: ["rowData"]
};
</script>