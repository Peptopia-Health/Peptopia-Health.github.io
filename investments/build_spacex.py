#!/usr/bin/env python3
"""Build investments/spacex.html — SPCX poster mirroring nvda.html's design system.
Banner header, banner CSS/JS, and poster CSS are lifted verbatim from nvda.html."""
import re, pathlib

NV = pathlib.Path('/home/hatch/workspace/investments/nvda.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/investments/spacex.html')

poster_css = re.search(r'<style>(.*?)</style>', NV, re.S).group(1)
banner_css = re.search(r'<style id="peptopia-banner-css">(.*?)</style>', NV, re.S).group(1)
banner_hdr = re.search(r'<header class="peptopia-hdr">.*?</header>', NV, re.S).group(0)
banner_js = re.search(r'<script id="peptopia-banner-js">(.*?)</script>', NV, re.S).group(1)

TV = 'https://www.tradingview.com/news/benzinga:eec79354c094b:0-elon-musk-spacex-pledge-18-billion-in-shares-to-trump-accounts-as-fcc-approves-1-million-starmind-orbital-ai-satellites-here-s-who-benefits/'
LB = 'https://longbridge.com/en/news/306878976'
NQ = 'https://www.nasdaq.com/articles/hundreds-millions-spacex-shares-become-eligible-sale-dec-8-should-you-buy-then'
CR = 'https://clearank.com/stock/spcx-spacex/'

body = f'''
  <!-- HERO -->
  <header class="hero">
    <div class="row" style="justify-content:space-between">
      <span class="chip tint-mint">🚀 SPCX DAILY POSTER</span>
      <span style="display:inline-flex;gap:6px">
        <span class="chip">Thu · Nov 26, 2026</span>
      </span>
    </div>
    <div class="row" style="margin-top:8px;gap:14px">
      <div>
        <h1><a href="https://www.spacex.com" target="_blank" rel="noopener">SpaceX · SPCX</a></h1>
        <div class="sub">Thanksgiving — markets closed. The plan is decided and the price is not there yet: $127.44 last close, your line is $110, and the December 8 unlock comes first.</div>
      </div>
    </div>
    <div class="row" style="margin-top:8px;gap:12px">
      <span class="price">$127.44</span>
      <span class="chg" style="color:#0E7A28">▲ $1.63 · +1.30% Wed close</span>
      <span class="meta">Wed Nov 25 close · Mkt cap ≈ $1.81T · Beta 2.05 · IPO $135 · Jun 12, 2026</span>
    </div>
    <div class="bar-wrap">
      <div class="bar"><div class="mark" style="left:19%"></div></div>
      <div class="bar-lab"><span>52-wk low $104.83</span><span>◉ Close: $127.44</span><span>52-wk high $225.64</span></div>
    </div>
  </header>

  <!-- HERO STATEMENTS -->
  <div class="grid2">
    <article class="hero-card hc-pos">
      <span class="tag g">▲ Hero · Positive</span>
      <h3>FCC clears Starmind — up to 1 million orbital AI satellites — as SpaceX and Musk pledge $18 billion in shares to Trump Accounts</h3>
      <p>The FCC has approved SpaceX's Starmind constellation of dedicated AI compute satellites, allowing up to 1 million orbital compute modules — a first US permit for space-based AI computing, and a direct expansion of the AI infrastructure story. SpaceX also announced it will donate one newly issued Class A share to every active Trump Account, with Musk personally matching and President Gwynne Shotwell adding 2 million shares: about 142 million shares, worth over $18 billion at Wednesday's close. SPCX rose 1.30% Wednesday against a falling market. <a href="{TV}">TradingView — Starmind approval &amp; $18B pledge</a> · <a href="{LB}">Longbridge — SPCX defies the market</a></p>
    </article>
    <article class="hero-card hc-neg">
      <span class="tag r">▼ Hero · Negative</span>
      <h3>797.6 million shares unlock December 8 — the biggest supply test since August, twelve days out</h3>
      <p>The final standard lock-up tranche releases up to 797.6 million shares on December 8, taking the tradable float to roughly 40% of the company. Earlier unlocks weighed on the price: the stock bottomed at $104.83 around the August 6 tranche and fell 9% on the October 22 release. Add investor pushback this week over a possible Tesla merger — narrative, not a filing — and the near-term path runs through a known supply event, not around it. <a href="{NQ}">Nasdaq — hundreds of millions of shares become eligible Dec. 8</a></p>
    </article>
  </div>

  <!-- SENTIMENT -->
  <section class="card">
    <h2>🧭 Sentiment &amp; Direction</h2>
    <div style="display:flex;flex-wrap:wrap;gap:6px;margin-bottom:6px">
      <span class="chip tint-green">Wed: +1.30% to $127.44</span>
      <span class="chip tint-red">Past month: −13.25%</span>
      <span class="chip tint-blue">Jefferies: Buy · $210 target (Nov 23)</span>
      <span class="chip tint-gold">Below the $135 IPO price</span>
      <span class="chip tint-lilac">Next catalyst: Dec 8 unlock · ~798M shares</span>
    </div>
    <p><strong>Read (sentiment, not fact):</strong> the headlines are loud and mostly kind — an FCC first, an $18 billion pledge, a fresh Buy initiation — while the stock still sits below its IPO price and 44% under its June high. That gap is the story-stock premium deflating on schedule. Your plan does not need the headlines to be wrong; it needs December 8 to do its work.</p>
  </section>

  <!-- 1 · OVERVIEW -->
  <section class="card">
    <h2>1 · Market Overview &amp; Key Moves</h2>
    <table>
      <tr><td>IPO price (Jun 11, 2026)</td><td class="n">$135</td></tr>
      <tr><td>First-day close</td><td class="n">≈ $161</td></tr>
      <tr><td>Post-IPO high (Jun 16)</td><td class="n">$225.64</td></tr>
      <tr><td>Post-IPO low (Aug 3)</td><td class="n">$104.83</td></tr>
      <tr><td>Latest close (Nov 25)</td><td class="n">$127.44</td></tr>
      <tr><td>Market value</td><td class="n">≈ $1.81T</td></tr>
      <tr><td>Beta</td><td class="n">2.05</td></tr>
      <tr><td>Q3 2026 revenue</td><td class="n">$14.6B · +161% YoY</td></tr>
      <tr><td>Starlink, 2025</td><td class="n">$11.4B · 61% of revenue</td></tr>
      <tr><td>2025 full year</td><td class="n">$18.7B revenue · $2.6B operating loss</td></tr>
      <tr><td>Index</td><td class="n">Nasdaq-100 since Jul 7, 2026</td></tr>
    </table>
    <p style="margin-top:6px">Starlink is the business: the only profitable segment, 13.6 million subscribers by Q3 2026, connectivity running at a ~$21 billion annualized pace with a 45.1% operating margin. The losses live in Starship and AI spending. SpaceX absorbed xAI in February 2026, and the FCC's Starmind approval this week pushes the same AI build-out into orbit.</p>
  </section>

  <!-- 2 · HIS PLAN -->
  <section class="card">
    <h2>2 · Your Plan — Decided</h2>
    <table>
      <tr><td>Decision (Nov 26, 2026)</td><td class="n">Own SPCX · $30,000 position</td></tr>
      <tr><td>Status</td><td class="n">Waiting for $110 · last close $127.44</td></tr>
      <tr><td>Limit line</td><td class="n">$110 / share (≈ 272 shares)</td></tr>
      <tr><td>Walk away above</td><td class="n">$135 · the IPO price</td></tr>
      <tr><td>Funded by</td><td class="n">Novo Nordisk trim · Rollover IRA</td></tr>
      <tr><td>Before Dec 8 unlock</td><td class="n">Do not chase</td></tr>
    </table>
    <p style="margin-top:6px">The decision is made, in your terms: the future is rooted in AI and the companies that make it available, and you prefer this risk over waiting years for Novo Nordisk to recover. The Novo trim happens inside the Rollover IRA, so the swap costs no tax, and SPCX is bought in the same account. What has <em>not</em> happened: no trade has been placed. Execution is your own action, and the plan stays staged until the price comes to the line — a limit order at $110 left in place through December lets the supply event do the work. Headlines do not move the line: above $135, the answer is no.</p>
  </section>

  <!-- 3 · POSITION SIZING -->
  <section class="card">
    <h2>3 · Position Sizing</h2>
    <div class="grid3">
      <div class="stat"><div class="v">$30,000</div><div class="k">Position</div></div>
      <div class="stat"><div class="v">2.6%</div><div class="k">Of $1,149,680 portfolio</div></div>
      <div class="stat"><div class="v">≈ 272 sh</div><div class="k">At the $110 line</div></div>
    </div>
    <p>Even a total loss would not touch the retire-at-57 plan, the guaranteed income floor, or health coverage. That size is the only reason a name this speculative fits the portfolio at all.</p>
  </section>

  <!-- 4 · RISK NOTES -->
  <section class="card">
    <h2>4 · Risk Notes</h2>
    <ul>
      <li><strong>Valuation:</strong> ≈ 95× trailing 2025 sales. A skeptical sum-of-the-parts model puts fair value near $32 a share — the stock could fall ~75% and still not be cheap on that math.</li>
      <li><strong>Volatility:</strong> beta 2.05 and a 52-week range of $104.83–$225.64. A $30,000 position can be a $20,000 position in a bad quarter with nothing "wrong."</li>
      <li><strong>Lock-up calendar:</strong> ~798M shares release December 8, 2026; extended lock-ups run into 2027, and Musk's ~6.4 billion shares unlock June 12, 2027.</li>
      <li><strong>Governance:</strong> Musk holds 48.4% of the equity and 82.4% of the voting power through 10-vote Class B stock. Public shareholders have effectively no voice.</li>
      <li><strong>Profitability:</strong> a $2.6B operating loss in 2025 and a $4.27B net loss in Q1 2026, against one profitable quarter since (Q3 2026, +$0.45 EPS). Starship and AI spending is enormous and open-ended.</li>
      <li><strong>Access:</strong> buy SPCX directly at Fidelity — it trades on Nasdaq like any stock. Skip the wrappers: DXYZ traded at a 151% premium to NAV in May 2026 while holding only 10.59% SpaceX.</li>
    </ul>
  </section>

  <!-- COACH -->
  <section class="coach">
    <h2>🎯 The Bottom Line</h2>
    <p>This is a patience trade, not a chase — the decision is made and the price has not arrived. Your $110 limit line sits under the IPO price with the December 8 unlock still ahead, so let the supply come to you. Above $135 the answer stays no, and the $30,000 stays a Novo trim inside the Rollover IRA or stays unspent.</p>
  </section>

  <!-- SOURCES -->
  <section class="card srcs">
    <h2>🔗 Sources</h2>
    <p><a href="{TV}">TradingView / Benzinga — FCC Starmind approval &amp; $18B Trump Account pledge</a> · <a href="{LB}">Longbridge — SPCX +1.30% close, Nov 25</a> · <a href="{NQ}">Nasdaq — Dec. 8 lock-up release, 797.6M shares</a> · <a href="{CR}">Clearank — SPCX snapshot &amp; analyst targets</a> · Market data: Finnhub (Nov 25 close $127.44, beta 2.05, 52-wk range) · Full analysis on file: SpaceX Analysis, Nov 26, 2026</p>
  </section>

  <p class="foot">SPCX poster · Finance Portal · Prices from market data, can move after publication · Research summary for your own portfolio — not financial advice.</p>
'''

html = f'''<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SPCX Daily Poster — Thursday, November 26, 2026</title>
<link rel="apple-touch-icon" href="/Tuscarora_Arboretum/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@700;800&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700&display=swap" rel="stylesheet">
<style>{poster_css}</style>
<style id="peptopia-banner-css">{banner_css}</style>
</head>
<body>
<div class="poster">
{banner_hdr}
{body}
</div>
<script id="peptopia-banner-js">{banner_js}</script>
</body>
</html>'''

OUT.write_text(html)
print("wrote", OUT, len(html), "bytes")
