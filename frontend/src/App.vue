<template>
  <div>
    <button
      class="btn btn-primary btn-margin"
      @click="sayHello()">
      Log In
    </button>
    {{message}}
    <br>
  </div>
</template>
<script>
import ModelService from './model/ModelService'
const modelService = new ModelService()

export default {
  name: 'App',
  data () {
    return { message: 'Initial Name' }
  },
  methods: {
    sayHello () {
      modelService.sayHello()
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
