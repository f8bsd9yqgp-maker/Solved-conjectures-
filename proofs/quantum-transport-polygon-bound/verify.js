// Run with Node.js: node verify.js
let count = 0;
let seed = 11262026;
const rand = () => {
  seed = (Math.imul(seed, 1664525) + 1013904223) >>> 0;
  return seed;
};
for (let n = 3; n <= 10; n++) {
  for (const q of [2, 3, 4, 6]) {
    for (let t = 0; t < 30; t++) {
      const x = [0n];
      for (let i = 1; i < n; i++) x.push(x[i-1] + BigInt(1 + rand() % 25));
      const w = (i,j) => (x[j]-x[i]) ** BigInt(q);
      const S = 2520n; // common denominator for chain sizes 2 through 10
      let D = 0n;
      for (let mask = 1; mask < (1 << n); mask++) {
        const a = [];
        for (let i = 0; i < n; i++) if ((mask >> i) & 1) a.push(i);
        if (a.length < 2) continue;
        let d = w(a[0], a[a.length-1]);
        for (let k = 1; k < a.length; k++) d -= w(a[k-1],a[k]);
        d *= S / BigInt(a.length);
        if (d > D) D = d;
      }
      const y = Array(n).fill(0n);
      for (let k = 0; k < n; k++) {
        for (let i = 0; i < n; i++) {
          for (let j = 0; j < n; j++) {
            if (i === j) continue;
            const c = D + (i < j ? w(i,j) : -w(j,i)) * S;
            if (y[j] > y[i] + c) y[j] = y[i] + c;
          }
        }
      }
      for (let i = 1; i < n; i++) if (y[i] < y[i-1]) y[i] = y[i-1];
      let err = 0n;
      for (let i = 0; i < n; i++) {
        for (let j = i+1; j < n; j++) {
          let a = y[j] - y[i] - w(i,j)*S;
          if (a < 0n) a = -a;
          if (a > err) err = a;
        }
      }
      if (err !== D) throw new Error("Exact error mismatch: n="+n+", q="+q+", t="+t);
      count++;
    }
  }
}
if (count !== 960) throw new Error("Unexpected test count");
console.log("PASS: " + count + " exact instances");
