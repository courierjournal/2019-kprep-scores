<template>
  <div id="app">
    <main>
      <section class="app-header">
        <h1>2019 K-PREP test scores</h1>
        <p>
          The Kentucky Performance Rating for Educational Progress (K-PREP) is here!

        </p>
      </section>
      <section class="app-explainer-new">
        <h2>Whats new for 2019</h2>
        <ul>
          <li>
            In an effort to help more easily guage the overall performance of a school, The Kentucky
            Department of Education has included a star rating system which assigns 1 and 5 stars based
            based on a combination of factors.
            <a
              href="#"
            >Read more about how this rating is calculated.</a>
          </li>
          <li>
            In keeping with federal standards,
            the designation of
            <i>
              Targeted Support
              and Improvement
            </i> (TSI) has been renamed to
            <i>Additional Targeted Support and Improvement</i> (ATSI).
          </li>
        </ul>
      </section>
      <section class="app-explainer-designations">
        <h2>How the designations work</h2>
        <p>
          Schools will be identified only for the federally-required accountability designations of Targeted Support and Improvement (TSI) – those with one or more low-performing groups – and Comprehensive Support and Improvement (CSI) – those in the bottom 5 percent of performance by level (elementary, middle or high); or that have a 4- year graduation rate of less than 80 percent. Schools designated as TSI and CSI will have to develop improvement plans and CSI schools will be provided additional support.
          <a
            href="https://www.courier-journal.com/story/news/education/2018/09/26/kentucky-school-ratings-system-what-csi-tsi-mean/1427412002/"
          >Read more about how these designations work</a>.
        </p>
      </section>
      <section class="app-database">
        <h2>Search the database of Kentucky schools</h2>
        
        <SearchBar />
        <DataTable :data="ScoreData" />
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
import ScoreData from "@/data/2019-kprep-scores.json";

export default {
  name: "app",
  components: { SearchBar, DataTable },
  data() {
    return {
      ScoreData
    };
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
