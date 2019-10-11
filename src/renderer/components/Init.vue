<template>
  <div id="app" style="height: 100%">
    <div class="app-wrapper">
      RPC Server Initializing...
    </div>
  </div>
</template>

<script>
export default {
  async created () {
    while (true) {
      try {
        let connected = await this.rpcClient.checkConnection()
        if (connected) {
          this.$router.push({
            name: 'main'
          })
          break
        }
      } catch (err) {
        console.log(err)
      }
    }
  }
}
</script>

<style scoped>
  .app-wrapper {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
</style>