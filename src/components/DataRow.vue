<template>
  <div>
    <div class="tr">
      <div class="td">
        <div class="school-name">{{rowData.n}}</div>
        <div class="school-district">{{rowData.d}}</div>
      </div>
      <div class="td">
        {{rowData.c}}
        <br />
        <span class="classification-reason">{{rowData.r}}</span>
      </div>
      <div class="td">
        <div class="star-container" :title="getTitle">
          <span class="full-stars" v-for="index in getStars[0]" :key="'f' + index">★</span>
          <span class="empty-stars" v-for="index in getStars[1]" :key="'e' + index">★</span>
        </div>
      </div>
      <div class="td">
        <div
          class="expand-button"
          :class="{ active: rowExpanded }"
          @click="rowExpanded = !rowExpanded"
        >+</div>
      </div>
    </div>
    <div class="tr" v-if="rowExpanded">
      <div class="expanded-container">
        <div v-if="rowData.hs.g" class="high-school-data">
          <div>Graduation Rate: {{rowData.hs.g}}%</div>
          <div>Transition Readiness Rate: {{rowData.hs.t}}%</div>
        </div>
        <table>
          <thead>
            <tr>
              <td></td>
              <td>Math</td>
              <td>Change*</td>
              <td>Reading</td>
              <td>Change*</td>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Total</td>
              <td>{{rowData.t[1][0]}}</td>
              <td :class="getStyle(rowData.t[3][0])">{{getDiff(rowData.t[3][0])}}</td>
              <td>{{rowData.t[0][0]}}</td>
              <td :class="getStyle(rowData.t[2][0])">{{getDiff(rowData.t[2][0])}}</td>
            </tr>
            <tr>
              <td>White Students</td>
              <td>{{rowData.t[1][1]}}</td>
              <td :class="getStyle(rowData.t[3][1])">{{getDiff(rowData.t[3][1])}}</td>
              <td>{{rowData.t[0][1]}}</td>
              <td :class="getStyle(rowData.t[2][1])">{{getDiff(rowData.t[2][1])}}</td>
            </tr>
            <tr>
              <td>Black Students</td>
              <td>{{rowData.t[1][2]}}</td>
              <td :class="getStyle(rowData.t[3][2])">{{getDiff(rowData.t[3][2])}}</td>
              <td>{{rowData.t[0][2]}}</td>
              <td :class="getStyle(rowData.t[2][2])">{{getDiff(rowData.t[2][2])}}</td>
            </tr>
            <tr>
              <td>Non-Economically Disadvantaged</td>
              <td>{{rowData.t[1][3]}}</td>
              <td :class="getStyle(rowData.t[3][3])">{{getDiff(rowData.t[3][3])}}</td>
              <td>{{rowData.t[0][3]}}</td>
              <td :class="getStyle(rowData.t[2][3])">{{getDiff(rowData.t[2][3])}}</td>
            </tr>
            <tr>
              <td>Economically Disadvantaged</td>
              <td>{{rowData.t[1][4]}}</td>
              <td :class="getStyle(rowData.t[3][4])">{{getDiff(rowData.t[3][4])}}</td>
              <td>{{rowData.t[0][4]}}</td>
              <td :class="getStyle(rowData.t[2][4])">{{getDiff(rowData.t[2][4])}}</td>
            </tr>
            <tr>
              <td>Non-English Learners</td>
              <td>{{rowData.t[1][5]}}</td>
              <td :class="getStyle(rowData.t[3][5])">{{getDiff(rowData.t[3][5])}}</td>
              <td>{{rowData.t[0][5]}}</td>
              <td :class="getStyle(rowData.t[2][5])">{{getDiff(rowData.t[2][5])}}</td>
            </tr>
            <tr>
              <td>English Learners</td>
              <td>{{rowData.t[1][6]}}</td>
              <td :class="getStyle(rowData.t[3][6])">{{getDiff(rowData.t[3][6])}}</td>
              <td>{{rowData.t[0][6]}}</td>
              <td :class="getStyle(rowData.t[2][6])">{{getDiff(rowData.t[2][6])}}</td>
            </tr>
            <tr>
              <td>No Disabilities</td>
              <td>{{rowData.t[1][7]}}</td>
              <td :class="getStyle(rowData.t[3][7])">{{getDiff(rowData.t[3][7])}}</td>
              <td>{{rowData.t[0][7]}}</td>
              <td :class="getStyle(rowData.t[2][7])">{{getDiff(rowData.t[2][7])}}</td>
            </tr>
            <tr>
              <td>Disabilities (IEP)</td>
              <td>{{rowData.t[1][8]}}</td>
              <td :class="getStyle(rowData.t[3][8])">{{getDiff(rowData.t[3][8])}}</td>
              <td>{{rowData.t[0][8]}}</td>
              <td :class="getStyle(rowData.t[2][8])">{{getDiff(rowData.t[2][8])}}</td>
            </tr>
          </tbody>
        </table>
        <aside>*Represents the change in points from the prior year</aside>
      </div>
    </div>
  </div>
</template>

<script>
import { getDiffieHellman } from "crypto";
export default {
  name: "DataRow",
  props: ["rowData"],
  computed: {
    getStars() {
      let fullStars = this.rowData.s;
      let emptyStars = 5 - fullStars;
      return [fullStars, emptyStars];
    },
    getTitle() {
      return `${this.rowData.s} stars`;
    }
  },
  data() {
    return {
      rowExpanded: false
    };
  },
  methods: {
    getDiff(val) {
      if (val > 0) {
        return "+" + val;
      }
      if (val <= 0) {
        return val;
      }
    },
    getStyle(val) {
      if (val > 0) {
        return "positive";
      }
      if (val < 0) {
        return "negative";
      }
    }
  },
  watch:{
    rowData: function(){
      this.rowExpanded = false;
    }
  }
};
</script>

<style>
.school-name {
  font-weight: bold;
}

.school-district {
  font-size: 0.8rem;
}

.star-container {
  font-size: 1.5rem;
  display: inline-block;
  cursor: pointer;
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
  user-select: none;
}

.expand-button.active {
  background-color: var(--gannett-grey);
  transform: rotate(45deg);
}

.expanded-container {
  padding: 1em;
  width: 100%;
  transition: height 0.5s;
  text-align: center;
  overflow-x: scroll;
}

.classification-reason {
  font-style: italic;
  font-size: 0.8em;
}

table {
  margin: 0 auto;
  max-width: 80%;
  border-collapse: collapse;
  font-size: 0.9rem;
}

td:first-child {
  text-align: right;
  width: 30%;
  border-right: 2px solid #888;
}

td:nth-child(3) {
  border-right: 2px solid #888;
}

td {
  width: 20%;
  padding: 0.3em;
}

thead {
  font-weight: bold;
}
thead > tr {
  border-bottom: 2px solid #888;
}

tbody > tr:nth-child(odd) {
  background-color: #e0e0e0;
  border-bottom:1px solid #aaa;
}

.high-school-data {
  padding: 1em;
  display: flex;
  margin: 1em;
  justify-content: space-evenly;
}

.positive {
  color: #43a047;
}

.negative {
  color: red;
}
</style>