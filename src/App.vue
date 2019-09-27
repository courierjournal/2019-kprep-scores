<template>
  <div id="app">
    <main>
      <section class="app-header">
        <h1>2019 KPREP test scores</h1>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse elementum nibh congue
          arcu commodo, at consequat nulla vehicula. Donec accumsan, nisi eu accumsan facilisis, sapien
          tellus ultrices arcu, quis hendrerit diam neque sit amet nisi. Interdum et malesuada fames
          ac ante ipsum primis in faucibus. Ut a dolor efficitur, tempus lorem sed, laoreet libero.
          Mauris non rhoncus justo. Pellentesque ut leo et risus maximus elementum id sed libero. Nam
          sit amet fermentum ligula, eu ultrices orci. Mauris est eros, auctor a aliquam eu, venenatis
          ac nunc. Nulla fringilla mi vitae dictum tempor. Etiam vitae urna sodales, auctor felis ut,
          euismod elit. Etiam vitae felis tortor. Sed eu viverra dui. Curabitur quis gravida erat.
          Aenean quis nisl risus.
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
        <p>
          The Kentucky Department of Education has released over 500,000(?) data points related to KPREP testing across the state.
          Courier Journal has parsed the most relevant data points into an easy to search database. Simply enter the name of the school
          or the district.
        </p>
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
import ScoreData from "@/data/dummy-scores.json";

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
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
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
  margin: 2em 0;
}

h1,
h2,
h3,
h4,
h5 {
  font-family: "Unify Sans", sans-serif;
}

h1 {
  font-size: 2.6em !important;
}

h1:after {
  background: var(--gannett-blue);
  content: "";
  display: block;
  height: 9px;
  margin: 10px 0;
  width: 45px;
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
</style>
