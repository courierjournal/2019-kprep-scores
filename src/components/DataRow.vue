<template>
  <tr>
    <td>
      <div class="school-name">{{rowData.n}}</div>
      <div class="school-district">{{rowData.d}}</div>
    </td>
    <td>{{rowData.e}}</td>
    <td>
      <div class="star-container">
        <span class="full-stars" v-for="index in getStars[0]" :key="'f'+ index">★</span>
        <span class="empty-stars" v-for="index in getStars[1]" :key="'e' + index">★</span>
      </div>
    </td>
    <td>
      <div
        class="expand-button"
        :class="{ active: rowExpanded }"
        @click="rowExpanded = !rowExpanded"
      >+</div>
    </td>
  </tr>
</template>

<script>
export default {
  name: "DataRow",
  props: ["rowData"],
  computed: {
    getStars() {
      let fullStars = this.rowData.s;
      let emptyStars = 5 - fullStars;
      return [fullStars, emptyStars];
    }
  },
  data() {
    return {
      rowExpanded: false
    };
  }
};
</script>

<style>
.school-name{
    font-weight:bold;
    font-size:1.1rem;
}
tr > td {
  padding: 1em;
}

td:first-child {
  text-align: left;
}

td:nth-child(2) {
  text-align: left;
}

td:nth-child(3) {
  text-align: center;
}

td:last-child {
  text-align: center;
}

.star-container {
  font-size: 1.5rem;
  display: inline-block;
}

.full-stars {
  color: #ffa000;
}

.empty-stars {
  color: #aaa;
}

.expand-button {
  text-align: center;
  font-weight: bold;
  font-size: 20px;
  display: inline-block;
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background-color: var(--gannett-blue);
  color: #fff;
  line-height: 27px;
  transition: transform 0.3s;
  cursor: pointer;
}

.expand-button.active {
  background-color: var(--gannett-grey);
  transform: rotate(45deg);
}
</style>