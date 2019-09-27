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
        <div class="explainer-popout">
          <h3>Whats new for 2019</h3>
          <p>
            Curabitur tortor risus, ornare nec dolor quis, semper consectetur nisi. Vivamus interdum,
            velit eu lacinia laoreet, odio nulla pulvinar velit, quis fringilla lectus nunc sed ligula.
            Quisque et ipsum ut magna pulvinar posuere. Nulla ut mi mattis, posuere risus ac, tristique
            libero. Morbi blandit non nulla a tristique. Morbi iaculis turpis nunc, eu dignissim quam
            dignissim a. Nam non magna at nunc porta dictum. Integer sit amet suscipit risus. Etiam sit
            amet porta erat, in maximus magna. Interdum et malesuada fames ac ante ipsum primis in faucibus.
            Proin fermentum rutrum urna, sit amet ultricies leo pretium eget.
          </p>
        </div>
      </section>
      <section class="app-database"></section>
    </main>
  </div>
</template>

<script>
export default {
  name: "app",
  components: {}
};
</script>

<style scoped>
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
