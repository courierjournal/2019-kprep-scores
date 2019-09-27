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
        <p>
          The Kentucky Department of Education has included a star rating system in an effort to help
          help more easily guage the overall performance of a school. The designation of Targeted Support 
          and Improvement (TSI) has been renamed to (ATSI).
          Curabitur tortor risus, ornare nec dolor quis, semper consectetur nisi. Vivamus interdum,
          velit eu lacinia laoreet, odio nulla pulvinar velit, quis fringilla lectus nunc sed ligula.
          Quisque et ipsum ut magna pulvinar posuere. Nulla ut mi mattis, posuere risus ac, tristique
          libero. Morbi blandit non nulla a tristique. Morbi iaculis turpis nunc, eu dignissim quam
          dignissim a. Nam non magna at nunc porta dictum. Integer sit amet suscipit risus. Etiam sit
          amet porta erat, in maximus magna. Interdum et malesuada fames ac ante ipsum primis in faucibus.
          Proin fermentum rutrum urna, sit amet ultricies leo pretium eget.
        </p>
      </section>
      <section class="app-explainer-designations">
        <h2>How the designations work</h2>
        <p>
          For the 2018 year the Kentucky Department of Education implemented two primary designations to schools
          with poor performance. <a href="https://www.courier-journal.com/story/news/education/2018/09/26/kentucky-school-ratings-system-what-csi-tsi-mean/1427412002/">
          Read more about how these designations work</a>.
          Morbi blandit non nulla a tristique. Morbi iaculis turpis nunc, eu dignissim quam
          dignissim a. Nam non magna at nunc porta dictum. Integer sit amet suscipit risus. Etiam sit
          amet porta erat, in maximus magna. Interdum et malesuada fames ac ante ipsum primis in faucibus.
        </p>
      </section>
      <section class="app-database">
        <h2>Star Search Database</h2>
        <p></p>
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
</style>
