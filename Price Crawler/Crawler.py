import requests, re

url = 'https://www.tgju.org/'

a = '''
 </div>
            
                <div class="container">
                    <div style="margin-bottom: 12px">
                        <ul class="info-bar mobile-hide">
                            <li id="l-gc30" style="" class=" high" onclick="if (!window.__cfRLUnblockHandlers) return false; window.location='markets/stock'" data-cf-modified-e45bdb7dc02285bf9c46ba80-="">
				<h3><em></em> بورس</h3>
				<span class="info-value">
					<span class="info-price">3,446,788</span>
				</span>
				<span class="info-change">(1.98%) 66,932</span>
			</li><li id="l-ons" style="" class=" low" onclick="if (!window.__cfRLUnblockHandlers) return false; window.location='profile/ons'" data-cf-modified-e45bdb7dc02285bf9c46ba80-="">
				<h3><em></em> انس طلا</h3>
				<span class="info-value">
					<span class="info-price">4,197.25</span>
				</span>
				<span class="info-change">(0.19%) 7.99</span>
			</li><li id="l-mesghal" style="" class=" high" onclick="if (!window.__cfRLUnblockHandlers) return false; window.location='gold-chart'" data-cf-modified-e45bdb7dc02285bf9c46ba80-="">
				<h3><em></em> مثقال طلا</h3>
				<span class="info-value">
					<span class="info-price">539,240,000</span>
				</span>
				<span class="info-change">(1.62%) 8,590,000</span>
			</li><li id="l-geram18" style="" class=" high" onclick="if (!window.__cfRLUnblockHandlers) return false; window.location='profile/geram18'" data-cf-modified-e45bdb7dc02285bf9c46ba80-="">
				<h3><em></em> طلا ۱۸</h3>
				<span class="info-value">
					<span class="info-price">124,496,000</span>
				</span>
				<span class="info-change">(1.65%) 2,016,000</span>
			</li><li id="l-sekee" style="" class=" high" onclick="if (!window.__cfRLUnblockHandlers) return false; window.location='coin'" data-cf-modified-e45bdb7dc02285bf9c46ba80-="">
				<h3><em></em> سکه</h3>
				<span class="info-value">
					<span class="info-price">1,302,800,000</span>
				</span>
				<span class="info-change">(2.34%) 29,850,000</span>
			</li><li id="l-price_dollar_rl" style="" class=" high" onclick="if (!window.__cfRLUnblockHandlers) return false; window.location='قیمت-دلار'" data-cf-modified-e45bdb7dc02285bf9c46ba80-="">
				<h3><em></em> دلار</h3>
				<span class="info-value">
					<span class="info-price">1,219,950</span>
				</span>
				<span class="info-change">(1.91%) 22,900</span>
			</li><li id="l-oil_brent" style="" class=" high tablet-hide" onclick="if (!window.__cfRLUnblockHandlers) return false; window.location='energy'" data-cf-modified-e45bdb7dc02285bf9c46ba80-="">
				<h3><em></em> نفت برنت</h3>
				<span class="info-value">
					<span class="info-price">63.75</span>
				</span>
				<span class="info-change">(0.02%) 0.01</span>
			</li><li id="l-crypto-tether-irr" style="" class=" high" onclick="if (!window.__cfRLUnblockHandlers) return false; window.location='profile/crypto-tether'" data-cf-modified-e45bdb7dc02285bf9c46ba80-="">
				<h3><em></em> تتر</h3>
				<span class="info-value">
					<span class="info-price">1,232,050</span>
				</span>
				<span class="info-change">(1.49%) 18,070</span>
			</li><li id="l-crypto-bitcoin" style="margin-left: 0 !important;" class=" low" onclick="if (!window.__cfRLUnblockHandlers) return false; window.location='crypto'" data-cf-modified-e45bdb7dc02285bf9c46ba80-="">
				<h3><em></em> بیت کوین</h3>
				<span class="info-value">
					<span class="info-price">89615.64</span>
				</span>
				<span class="info-change">(0.08%) 70.15</span>
			</li>                        </ul>
                        <div class="clear"></div>
                    </div>
                </div>

                                    <div class="fs-row">
                        <div class="fs-row">
                            <div class="fs-cell fs-sm-12 fs-md-12 fs-lg-12 fs-xl-12">
                                <ul class="advertise" id="advertise-place-41" style="margin-bottom: 8px;">
                                    <li data-row="0" data-place-name="03. شبکه اطلاع رسانی / C" class="show"><a target="_blank" href="https://tmdn.ir/fmi"><img id="ad-v9j9ok1cmbzu9g2rho79" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" data-ad-img-src="https://static.tgju.org/advertisement/comp-3-iteration-1-1762264335.gif" alt="تمدن" class="ad-hide"></a>
			<script type="e45bdb7dc02285bf9c46ba80-text/javascript">
			ad = document.getElementById("ad-v9j9ok1cmbzu9g2rho79");
			if ((ad.parentNode.parentNode.parentNode.className.indexOf("advertise-mobile") !== -1 && viewport_size() < 758)
				|| (ad.parentNode.parentNode.parentNode.className.indexOf("advertise-mobile") === -1 && viewport_size() > 758)
				|| (ad.parentNode.parentNode.parentNode.className.indexOf("advertise-all") !== -1)
			) {
				ad.setAttribute("src", ad.getAttribute("data-ad-img-src"));
				ad.setAttribute("class", "");
			}
			</script>
			</li>                                </ul>
                            </div>
                        </div>

'''
c = requests.get(url)

if c.status_code == 200:
    a = c.text
else:
    print('sth wrong!!!!!')

b = r'em>.*> ([^a-z]*)<.*\n.*\n.*price\">([^a-z]*)<'
regex = re.compile(b)
res = regex.findall(a)
print(res)