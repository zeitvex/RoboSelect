---
layout: page
sidebar: false
outline: false
titleTemplate: false
---


<div class="home">
  <section class="home-hero">
    <div class="home-kicker">机器人部件选择社区</div>
    <h1>选部件，先看参数，再看<em>用过的人怎么说</em>。</h1>
    <p>
      每个部件一页：左边是官方参数（带来源等级与口径），右边是真实使用者的评分与评价。
      不收佣金、不卖零件，所以判定不必讨好谁。
    </p>
    <div class="home-cta">
      <a class="home-btn" href="/catalog">进部件库 →</a>
      <a class="home-btn ghost" href="/suppliers">找加工与供应商</a>
      <a class="home-btn ghost" href="/semantics">参数口径怎么读</a>
    </div>
  </section>

  <section class="home-stats">
    <div><b>131</b><span>在库部件</span></div>
    <div><b>11</b><span>有数据的品类 · 共 13 类</span></div>
    <div><b>97</b><span>逐项核对过厂商手册（A 级）</span></div>
    <div><b>149</b><span>加工与标准件供应商</span></div>
  </section>

  <section class="home-cats">
    <h2>按品类</h2>
    <div class="home-cat-grid"><a class="hc" href="/parts/actuator/"><b>关节电机</b><span>46</span><em>选型主战场</em></a>
<a class="hc" href="/parts/servo/"><b>舵机</b><span>5</span><em>串行总线 / PWM</em></a>
<a class="hc" href="/parts/controller_high/"><b>上位机</b><span>9</span><em>推理与感知</em></a>
<a class="hc" href="/parts/controller_low/"><b>下位机</b><span>14</span><em>力矩闭环</em></a>
<a class="hc" href="/parts/esc/"><b>电调</b><span>3</span><em>驱动器 / 调速器</em></a>
<a class="hc" href="/parts/imu/"><b>IMU</b><span>7</span><em>姿态与振动</em></a>
<a class="hc" href="/parts/sensor/"><b>传感器</b><span>3</span><em>ToF / 电流 / 霍尔</em></a>
<a class="hc" href="/parts/lidar/"><b>激光雷达</b><span>10</span><em>地形与建图</em></a>
<a class="hc" href="/parts/camera/"><b>深度相机</b><span>14</span><em>视觉感知</em></a>
<a class="hc" href="/parts/battery/"><b>电池</b><span>待收录</span><em>待收录</em></a>
<a class="hc" href="/parts/wiring/"><b>线束</b><span>2</span><em>待收录</em></a>
<a class="hc" href="/parts/module/"><b>其余模块</b><span>待收录</span><em>力触觉 / 编码器</em></a>
<a class="hc" href="/parts/chip/"><b>硬件芯片</b><span>18</span><em>MCU / 驱动 / 收发器</em></a></div>
    <p class="home-note">
      「待收录」不是漏了 —— 是没有可信来源。宁可空着，也不拿论文里的典型值充数。
    </p>
  </section>

  <section class="home-how">
    <h2>这一页该怎么用</h2>
    <div class="home-how-grid">
      <div>
        <b>1 · 先看官方参数</b>
        <p>来源等级 <code>A</code> 表示逐项对过厂商手册。缺的字段写 <code>—</code>，
        不猜、不用额定代替峰值。每个数都能查到「谁在什么时候、凭什么改成了现在这样」。</p>
      </div>
      <div>
        <b>2 · 再看使用者的分</b>
        <p>评分走 GitHub issue，<strong>一人一件一票</strong>，装过机的单独统计。
        评论在部件页底部（GitHub Discussions），用来说明「为什么给这个分」。</p>
      </div>
      <div>
        <b>3 · 别只看峰值扭矩</b>
        <p>部件页会算扭矩密度、峰值/额定比、反射惯量占比。高减速比件通常前两项好看、
        第三项很糟 —— 那条腿会很「黏」。</p>
      </div>
    </div>
  </section>

  <section class="home-links">
    <a href="/parts/">按厂商浏览</a>
    <a href="/semantics">参数口径</a>
    <a href="/sources">数据来源与纪律</a>
  </section>
</div>

<style>
.home { max-width: 1180px; margin: 0 auto; padding: 2.2rem 1.5rem 4rem; }
.home-hero { padding: 1.2rem 0 1.8rem; border-bottom: 1px solid var(--vp-c-divider); }
.home-kicker {
  font-size: 0.72rem; letter-spacing: 0.12em; text-transform: uppercase;
  color: var(--vp-c-brand-1); font-weight: 700; margin-bottom: 0.6rem;
}
.home-hero h1 {
  font-size: clamp(1.6rem, 3.4vw, 2.5rem); line-height: 1.25; font-weight: 800;
  letter-spacing: -0.02em; margin: 0 0 0.8rem; border: none; padding: 0;
  color: var(--vp-c-text-1);
}
.home-hero h1 em {
  font-style: normal;
  background: linear-gradient(135deg, var(--vp-c-brand-1), #4fc1ff);
  -webkit-background-clip: text; background-clip: text; color: transparent;
}
.home-hero p { margin: 0 0 1.2rem; max-width: 62ch; font-size: 0.92rem;
  line-height: 1.85; color: var(--vp-c-text-2); }
.home-cta { display: flex; gap: 0.6rem; flex-wrap: wrap; }
.home-btn {
  font-size: 0.86rem; font-weight: 600; padding: 0.5rem 1.05rem; border-radius: 999px;
  background: var(--vp-c-brand-1); color: #fff; text-decoration: none;
}
.home-btn.ghost {
  background: transparent; color: var(--vp-c-text-1);
  border: 1px solid var(--vp-c-divider);
}
.home-btn:hover { text-decoration: none; opacity: 0.92; }

.home-stats {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
  gap: 1px; background: var(--vp-c-divider);
  border: 1px solid var(--vp-c-divider); border-radius: 12px; overflow: hidden;
  margin: 1.6rem 0;
}
.home-stats > div { background: var(--vp-c-bg); padding: 0.9rem 1rem; }
.home-stats b {
  display: block; font-size: 1.5rem; font-weight: 800; line-height: 1.1;
  color: var(--vp-c-brand-1); font-variant-numeric: tabular-nums;
}
.home-stats span { font-size: 0.74rem; color: var(--vp-c-text-3); }

.home h2 {
  font-size: 1.02rem; font-weight: 700; margin: 0 0 0.8rem;
  border: none; padding: 0; color: var(--vp-c-text-1);
}
.home-cat-grid {
  display: grid; grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); gap: 0.5rem;
}
.hc {
  display: flex; flex-direction: column; gap: 2px;
  border: 1px solid var(--vp-c-divider); border-radius: 10px;
  padding: 0.6rem 0.7rem; text-decoration: none;
  background: var(--vp-c-bg); transition: border-color 0.18s, transform 0.18s;
}
.hc:hover { border-color: var(--vp-c-brand-1); transform: translateY(-2px); text-decoration: none; }
.hc b { font-size: 0.84rem; color: var(--vp-c-text-1); }
.hc span { font-size: 0.74rem; color: var(--vp-c-brand-1); font-variant-numeric: tabular-nums; }
.hc em { font-size: 0.7rem; font-style: normal; color: var(--vp-c-text-3); }
.home-note { font-size: 0.74rem; color: var(--vp-c-text-3); margin-top: 0.7rem; }

.home-how-grid {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 0.8rem;
  margin-top: 0.4rem;
}
.home-how-grid > div {
  border-left: 3px solid var(--vp-c-brand-soft); padding: 0.1rem 0 0.1rem 0.8rem;
}
.home-how-grid b { font-size: 0.84rem; color: var(--vp-c-text-1); }
.home-how-grid p { font-size: 0.78rem; line-height: 1.8; color: var(--vp-c-text-2); margin: 0.3rem 0 0; }
.home-links {
  display: flex; flex-wrap: wrap; gap: 1.1rem; margin-top: 2.2rem;
  padding-top: 1.1rem; border-top: 1px solid var(--vp-c-divider);
  font-size: 0.8rem;
}
.home-links a { color: var(--vp-c-brand-1); }
</style>
