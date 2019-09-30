<template>
  <div id="app">
    <main>
      <section class="app-header">
        <h1>2019 K-PREP test scores</h1>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce nibh orci, pellentesque id lacinia non, dapibus ac nulla. Praesent eget interdum eros. Sed vel venenatis turpis. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Cras vestibulum blandit sodales. Nulla viverra tellus vitae purus maximus auctor. Donec et enim in orci ornare feugiat vitae sit amet arcu.</p>
      </section>
      <section class="app-explainer-new">
        <h2>Whats new for 2019</h2>
        <ul>
          <li>
            In an effort to help more easily gauge the overall performance of a school, The Kentucky
            Department of Education has included a star rating system which assigns 1 and 5 stars based
            based on a combination of factors.
            <a
              href="#"
            >Read more about how this rating is calculated.</a> (Can we explain this?)
          </li>
          <li>
            In keeping with federal standards,
            the classification of
            <i>
              Targeted Support
              and Improvement
            </i> (TSI) has been renamed to
            <i>Additional Targeted Support and Improvement</i> (ATSI).
          </li>
        </ul>
      </section>
      <section class="app-explainer-designations">
        <h2>How the classifications work</h2>
        <p>The federal government requires states to tract two categories of underachieving schools:</p>
        <ul>
          <li>ATSI: which are</li>
          <li>CSI: which are</li>
        </ul>
        <p>
          <a href="#">Read more about how these classifications work</a>. (Do we have an updated link?)
        </p>
      </section>
      <section class="app-database">
        <h2>Search the database of Kentucky schools</h2>

        <SearchBar @filter="setFilterQuery" />
        <DataTable :data="paginatedList" />
        <Paginate
          v-show="filteredList.length > paginate.itemsPerPage"
          :pageCount="paginate.pageCount"
          :click-handler="paginationControl"
        />
      </section>
      <section class="app-map">
        <h2>Map of Schools in Kentucky</h2>
      </section>
    </main>
  </div>
</template>

<script>
import SearchBar from "@/components/SearchBar";
import DataTable from "@/components/DataTable";
import Paginate from "vuejs-paginate";
import ScoreData from "@/data/2019-kprep-scores.json";

export default {
  name: "app",
  components: { SearchBar, DataTable, Paginate },
  data() {
    return {
      ScoreData,
      filterQuery: "",
      paginate: {
        itemsPerPage: 10,
        currentPage: 0,
        pageCount: 0
      }
    };
  },
  computed: {
    filteredList(query) {
      var search = this.filterQuery.toLowerCase().trim();
      if (!search) return this.ScoreData;
      return this.ScoreData.filter(o =>
        Object.keys(o).some(k => {
          return String(o[k])
            .toLowerCase()
            .includes(search.toLowerCase());
        })
      );
    },
    paginatedList() {
      let beginning = this.paginate.currentPage * this.paginate.itemsPerPage;
      let end = beginning + this.paginate.itemsPerPage;
      return this.filteredList.slice(beginning, end);
    }
  },
  methods: {
    setFilterQuery(query) {
      this.filterQuery = query;
      this.setPageCount();
    },
    paginationControl(e) {
      this.paginate.currentPage = e;
    },
    setPageCount() {
      this.paginate.pageCount =
        Math.floor(this.filteredList.length / this.paginate.itemsPerPage);
    }
  },
  created() {
    this.setPageCount();
  }
};
</script>

<style>
@font-face {
  font-family: "Unify Sans";
  src: url(https://www.gannett-cdn.com/gannett-web/global/fonts/unify/UnifySans_W_Bd.woff2);
  font-weight: 800;
}

:root {
  --gannett-blue: #009bff;
  --gannett-grey: #404040;
}

#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  color: #2c3e50;
  margin-top: 60px;
}

main {
  max-width: 1080px;
  margin: 0 auto;
}

.explainer-popout {
  padding: 1em;
  color: #004085;
  background-color: #cce5ff;
  padding: 0.75rem 1.25rem;
  margin-bottom: 1rem;
  border: 1px solid transparent;
  border-radius: 0.25rem;
}

section {
  margin: 3em 0;
}

h1,
h2,
h3,
h4,
h5 {
  font-family: "Unify Sans", sans-serif;
}

h1 {
  font-size: 2.3em !important;
}

h2 {
  font-size: 1.3em;
  border-left: 6px solid var(--gannett-blue);
  padding-left: 8px;
}

p,
ul {
  font-size: 1em;
  line-height: 1.3em;
  margin: 1em;
}

li {
  margin-bottom: 10px;
}

.app-header {
  text-align: center;
}

.app-header > p {
  font-size: 1.2em;
  max-width: 80%;
  margin: 0 auto;
  line-height: 30px;
  color: #555;
}
</style>
