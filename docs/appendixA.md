Appendix A: Named Actions
=========================

The following action sets are currently implemented.

Please note that the actions are realized using regular expressions. I decided not to show them in the following for a better readability and show the visible changes only.

| Action Name | From Opening String | From Closing String | To Opening String | To Closing String |
| ---- | ---- | ---- | ---- | ---- |
| quotes.english | ' | ' | &lsquo; | &rsquo; |
| | " | " | &ldquo; | &rdquo; |
| quotes.french | &lt; | &gt; | &lsaquo; | &rsaquo; |
| | &lt;&lt; | &gt;&gt; | &laquo; | &raquo; |
| quotes.german | ' | ' | &sbquo; | &rsquo; |
| | " | " | &bdquo; | &rdquo; |
| to_quotes | ' | ' | &lt;q&gt; | &lt;/q&gt; |
| | " | " | &lt;q&gt; | &lt;/q&gt; |
| | &lt;&lt; | &gt;&gt; | &lt;q&gt; | &lt;/q&gt; |
| | &lt; | &gt; | &lt;q&gt; | &lt;/q&gt; |
| commercial | (c) | | &copy; | |
| | (r) | | &reg; | |
| | (tm) | | &trade; | |
| dashes |  -  | | &mdash; | |
| | &lt;NUMBER&gt;-&lt;NUMBER&gt; | | &lt;NUMBER&gt;&ndash;&lt;NUMBER&gt; | |
| bullets | * | | &bull; | |
| ellipsis | ... | | &hellip; | |
| apostrophe | ' | | &apos; | |
| math | +/- | | &plusmn; | |
| | 1/2 | | &frac12; | |
| | 1/4 | | &frac14; | |
| | 3/4 | | &frac34; | |
| | ~ | | &asymp; | |
| | != | | &ne; | |
| | &lt;= | | &le; | |
| | &gt;= | | &ge; | |
| | &lt;NUMBER&gt;\*&lt;NUMBER&gt; | | &lt;NUMBER&gt;&times;&lt;NUMBER&gt; | |
| | &lt;NUMBER&gt;x&lt;NUMBER&gt; | | &lt;NUMBER&gt;&times;&lt;NUMBER&gt; | |
| | &lt;NUMBER&gt;/&lt;NUMBER&gt; | | &lt;NUMBER&gt;&divide;&lt;NUMBER&gt; | |
| dagger | ** | | &Dagger; | |
| | * | | &dagger; | |
| arrows | &lt;- | | &larr; | |
| | &lt;-- | | &larr; | |
| | -&gt; | | &rarr; | |
| | --&gt; | | &rarr; | |
| | &lt;= | | &lArr; | |
| | &lt;== | | &lArr; | |
| | =&gt; | | &rArr; | |
| | ==&gt; | | &rArr; | |
