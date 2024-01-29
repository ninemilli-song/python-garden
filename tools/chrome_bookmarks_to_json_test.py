import unittest
from bs4 import BeautifulSoup
from .chrome_bookmarks_to_json import get_dt_tree, get_dl_tree


class MyTestCase(unittest.TestCase):
    def test_dt(self):

        soup = BeautifulSoup('''
            <DT><H3 ADD_DATE=\"1616134925\" LAST_MODIFIED=\"1635215721\">素材</H3>
            <DL><p>
                <DT><A HREF="http://sc.chinaz.com/html/Icons/index_11.html" ADD_DATE="1313313612" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAAAi0lEQVQ4jZXS3Q2FIAwF4La4kMk1LuBE3Dlc4y6BG0DjKC7gz32AKKliynkDvpNCAhrroCrGuiNLCGHzuHkU+zHGOsrLzNwe3blsvtN9AJV0KVSlU0GvU0HoGf3dMXN8EokD+uyPuv8t1wS9ToXoNPqa8KgBQGh5pfes41BRiFpbOLWqkGsAwNrv/Qdemlx/uCDOPAAAAABJRU5ErkJggg==">图标 图标下载 桌面图标 ico图标 ico图标下载</A>
                <DT><A HREF="http://www.bitbug.net/" ADD_DATE="1338189417" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAACh0lEQVQ4jT2STUhUYRSGzznfd+/MnXEK/1IJlaiNSIUWKo1tjBAiomVom6Ciolq1SmphuKwWtamkRSC1KCkDt/05ZYWYpiWVaKEzWjP5M95758797ndaOHYWh/PC+x6exYusNQAAAAPgxgHAzBoREWhdMGgimVgckBs2QAAupBiREAtWBAQAXt8CCZABmREYGQCYAwRMO8lns/eW8n8QMeAAkBEZABBRMv8nAmZNJNxgpXeie8GZnUh9OLv7WkmkMuCgAMJMBSAAZiYUrnL6vt1Mu6nNZvmKn+6d7JlfmRUomHn9KwEWhogUun3TPV8WRyxZpFGFDSvtJu9OXk7aXwmJmRERT/XeymSzOc/Lq0BE7VD0V1NDaHQ8NzwSaWn2G+oxlXYy8xX3O29bIXMo/ZzeT471J16aALtqaxMfZ1694YXManGxqtrixqLgujwwEH39zlu1VzUzAFAsEjVIHt7ZeP34ydIiq7KstL50b3rJnpsTfl5/nnIzf1kLr6nr/JqnTSEp7/ubiqJdTx9WnOn4ubK0p3rH6cauGnPfQjIXVTXn4hctC5DpZPuRiCGU1iSFyLrOiXjbwKWrHa1tj14MPkkM7a8+iJCpL25trzsQixhh07xytEMKDliTp3yl+XtqbnT6h6PyWvmZnO0ENvueBvADlV1zHN+fXExqDQhAVbGSuq2VY/Mz3f0PPk1NHIq3djbHw4iVZeVRyzCEPNYSj0l54c4N1iiFwMfjI8iKUAjCQOlIOGQapu06nq+kIS0zRAjLtpPL51u31/+mt3IslUTcqCpCEGjNLIiIUGvWrAHAFHI552wrrbbKJbqejUSFkq6nsFAsQEQAzYDASnHIDA0vDf4DnVVPkY0fAHAAAAAASUVORK5CYII=">制作ico图标 | 在线ico图标转换工具 方便制作favicon.ico - 比特虫 - Bitbug.net</A>
            </DL><p>
        ''', 'html5lib')
        dt = soup.html.body.dt
        titles, bookmarks = get_dt_tree(dt)
        self.assertEqual(len(titles), 1)
        self.assertEqual(titles[0]['title'], '素材')
        self.assertEqual(titles[0]['add_date'], '1616134925')
        self.assertEqual(len(bookmarks), 2)
        self.assertEqual(bookmarks[0]['title'], '图标 图标下载 桌面图标 ico图标 ico图标下载')
        self.assertTrue(bookmarks[0]['icon'] is not None)

    def test_dl_sample(self):
        soup = BeautifulSoup('''
                    <DL><p>
            <DT><A HREF="http://www.sse.com.cn/" ADD_DATE="1507892328" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAC/0lEQVQ4jWWTX2hWdRzGP9/f97znvO/+5XE5YbIQxzZKCeaGXsTMGmEzQcjIIAiXdiEjQ6lQrxYoDC+c0IVQF3VnIwSrWRezfIVg6JBwLNSIYOvCmhuyv+/e95zz+3bhZkEPPJef5+r5CP9GADsE+RdgbwBdETSGUAngbgYjB2AMoB9cP/g16Ak8AD3r4EwVtNeARAghjgAhgbJgQ/NkJw/AgzXG9YMD7BPoq4LvI9iu4BVNQ43SkDANyKVV5HIxwTsxwfVh2AKYgQjAaeh+CkaqwNeAr0WCahx5MgpAiCKorQiJM4vmlLE7WfLSR7AsPRC1w88xdBYgrQOtE0dtkKP5w48lfnk3LvVmC/OkSUJiPgnDXFhCTjW++cZA0ALdQEcK3oE65/De0zI4KE19R1n5ZdxmPzghGtVatrmJrKagyw6/TPaWmZ0PzLldzgzAi6qW09TaDvW6pr6jrExO8ltXlzz96j7b8Ol5vHmmL33t0pWSqFrraG9vm24ze1dhm4Jl3rtNW7fSNfQVLsrLxGv70Hg9W679IIjIvdcPIlUF04YNGCY1zc3DQfOOHRrn8+TSVOL6evZcvChhHMvEqdNMj99h18SvOGDi8HsUdnbQfG7AzY6O2p9Xr4qvVCzoPn78IaUSVCqWD0OmikX+uvYjk19+Ya9cuSKFzc/wx4ULtrwwz3PnBmTm1i17ePOmBA0NSSYy7W5fvvxTaW5OfJZJZXGR8swMcWuL7SkWZdP+/fx944ZNffOtdAxdMgeUJie9lMt+fmrq98PHjk3IrFld8ezZ69mjR9sDSHNmGqoiS0skMzPy4Lth1rW12vrOTpLFRSSOk+ra2jBobT2x88iRQQF4HrqfhZEIfDX4AgR5oLBaA9LHz0sEojkYG4AXgRUHuHGzYnUUvR+qqlPNmar3qllFNVuAbEkkS1QR1agcBPfrN248iFn5fzK9DT0hnFFoj0BygK42hbKDoXk4+dl/ZFobeDKyG/JNsBfoCqDRQUXhrsHI56s681hAD/AP+2I3HPAB7ZYAAAAASUVORK5CYII=">上海证券交易所</A>
            <DT><A HREF="http://www.szse.cn/" ADD_DATE="1507892344" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAACYUlEQVQ4jY2SS0hUURzGf/9zT2N3fGbNKBLDFJOBQRlkxCRFUmEPemFQi2opLSKiF61yF0EiWUbRNojouZEoMgomsIc9IBdFuiiZtCztatPVuXNvi5xxxgz64MDh8H2/853DX5hOjTeWUVK6k8rIDvzmanYH4tP6AJ3Z1TSVY/oPU+hvYHgkTHUVFJmQohyYBLR1F6ALozSG7ucCxlIH8BJHSDlUrFzCeLiMoaRHyqWU47EQpt6Mz7eJhFuH/umj5dVsDi0dngTYY3U4BqEFc4muWsxA0iVueB/fP+g65I0l63G0wjD4s7SD1m5WgyalnNFK8WDX3rXMMBXFWvr92l3z7tPnkxiiMDToCYDWfVzYak0CwsNFgi6pWV5JdaSMH0nXNrVsv7TC38u6FhdDgdYTYQMM40XuJzqi8MGWDdUEZypM7Z3YX+XvBMBKlOA6E2GVfkJ7GqAAiBRbeF5ifW2EwEwV2xY2WwG49mWj5BdsUd9HkW8WMmjB4A+LnyO3cgGPmpzyYFFfKFjoBvzeQRFxA+1D1SiuSv8XJZ6HSrmocQdtJ8/ztMnKBQAL5wXfgtypyPe9PNg5urgij3t8jBfJLzt7bvocsU9nH2QA4dCcJ4icvdmbaJiVx2MtBOXZGxBJWxwR9vHhnJUNyMxB/fqq+99t53KeUlHBxf06hHR1Z4we3oFUT/NDpijTYHVtlS0QTdvjV+4irgvgeHj73d7mi1PDOQ2y9fx2jK/dvYiSuMCe6W7+q0FasY7X3L3SMa6Q1lTKWeT0nPlnOEcDtje/7fqLT77Ko6eIHJv7XyHgN8lz1NFX+w2CAAAAAElFTkSuQmCC">深圳证券交易所</A>
            <DT><A HREF="http://www.shenqigongshi.com/" ADD_DATE="1520159345" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAW0lEQVQ4jWN0cnL6z0Am2LdvHyMTuZphgGIDWJA5e/fuhbOdnZ2xiiMDRkZGVAOIAV9dzFH4gywMkAEufxNtALJfufecxGkA5V4g1qk4DSDWqbjAwEcjxQZQDACEAxVCI3QBTAAAAABJRU5ErkJggg==">股市神奇公式 - 选股三分钟，精挑三十只，安心三整年</A>
            <DT><A HREF="https://etrading.cxfund.com.cn/etrading/account/login/init" ADD_DATE="1528879177" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAACd0lEQVQ4jW1SS2sTYRS9M/NNZjLNo2maNEnbJG1Kgi1t0we+KFVMoQilKxVcClIUXNiFS3+CCwVXVlxbBBXEhWhXppIq0iINqalNKkk7eTSZmUySyWQeLqKtBs/mcjnncC+cg+m6Dv+izh/sbzzVtab/7C2j1dPG4m27JJb2Pj4S8/FqMZlaf9yUhDYBdnxBbUps/A2X+argNl0ukAgv0ZMPo+R0qPfOYthkNLRkqDU0RU7HVsr7UQBAdBmYYIn23XtZOywLn5NHh6Xqg6ULiMABANM0tcJu53beVSoyphyBIiDHxIuEKycZjZQhGj9w282RkOGyO+EMXrK4R7F8cu3nl2e62sQRQ1hP0WbP/fcotisAwLDPHgn3e+lcoPpKV0SMIL3TN4i5YYIx2zBNoi3ejk57rd7Iqe48LzG0YXzQURYbJiXnoOpIFxmbT+LzxPyogU0nh05fQ0jnMxtqJRW0FB3eqV6nPbbDxhJsNK0SHa6pgEvmkkqjhgNAo8bXxep+YgsjTYAjirGd7zkIdxd6OhmSwF2d9A+e5uqgyuJJDrqm7X1bT31PWzxnaKSrmbd95dWlkd2rMwGGpjZTnP5HiYfOXcEJsuUSilkuly0VWAwjAEdOSrAQXI6rtaLCcOQYmkVTC8tO/4Qi8QAYAEhVIbm55huZcfX3Nfg9re4HAMAwU1ffwPiytTeMcJzwjUWajZo7sFrMbAOAqsjF7G53t1FXm603poOu0OQcQ5EnSZMUM3/7SWL9uVxh/27OkMd6d2Dw+sVQS31iAACD0TwWuXmUicc/vf7N0ZaF2XBHl+//5TtGKZvY+rDS7/d7RhcZm7eN/QXigRCvjhNggQAAAABJRU5ErkJggg==">长信基金-登录</A>
            <DT><A HREF="https://e.gtfund.com/etrade/Index/mainpage" ADD_DATE="1528879366" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAACxUlEQVQ4jU2QT2icZRDGf/O+3/ftbprNdhMj2NK0eNAURKytR0GkV0EUURoK2pvQg/TSg+hBvUpvShHqHzwUFIkUPCh6kOLBs0ItabqmoiXbdjfZzX7/3nfGw6YhA8PMMPDwex4B+JJHn2745KNh/Fc9guKkSZeSAQ4hpUPBEEHNkUpKp4jk588x7icAxs5iks2/dOLNCzjnCZOc/365zpOnzxCris3rv7N8+ix4T9Xvs/bdD5SWXAT6AHzO7AtfZ4+FH19bqWIItZrZT6+cDWpm9WQSfn79XLDdKvqb4Uq6OL5MawnAATRpolXpbn+z6sa3/3Y6yVXL0oXR2Mp7D5zmpdOq1mq4pevffu9M8R6TPYGKIIKj0eriGxnOOwSHeI/4BACXpW7w101+ffsdkYgVNAGYfklQTExVVFXUDBUTM8NMUQzARERS1wAVaVKwRwAggGEg011MENntKS0i02kY7BLsCgRAcD5BEAwwgSmBsb/Ee2Tf7aYGEhQln9xHQwSZyjwkMDEAiXVNUd/f5d1noWJs2cwBe+69963ZPWhaVlOAGM1iNAHTuta5o0v2zPkLhrO9EB2GBAqSzqyd/OCiz7oHnW+3hUbDkvasZAvzJs2GuTR1M4cPuVMfvqvmzVJKm9ILJjS9H+fuxqVPyOZmiUUh1a2e3Pr0CjHPXbXWY/2zL0Ackzv/eIkyo5h7GD5f8cipFlzaYuBBEVDPXBrZDoLDcSAJjKKBeBJp0dkpyFfeYufuXqDHu92nZh4/ecfvbCf5ZNh5deNMb3X56hIFvNx7Y+PaE9fmF44t5NyF9fXfjq2NxzeAKACHFtrLmcqJ3mB79ch853nxcnyjP7x8dHHuxQhoqP/wLnm20nItjc3SZcnKxr0HHwMjB+Dq0aaKhMPt9pFay5uo/QlEC35LajeuBvnA48m0lfsQxsHqq8AI4H9PgGdXtAd7lAAAAABJRU5ErkJggg==">国泰基金</A>
            <DT><A HREF="http://www.thfund.com.cn/" ADD_DATE="1528879927" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAACjklEQVQ4jSXNz2tcZRQG4Pec77v3jnFi01byozU1JJS0zKhgXeiiaAuCBa3WjYiIUARRl4IrF3Xh1oUrV7oRiiKItFSIqGM3TakJJkhqG8FWkZCmM9FJ7cy93z3ndeHzDzxidIcoqEmgNUN0RxCHAMmGWVYAIMWTBSVE4RLh6v27mVnQAYxqpBsdWfh3aZkrayaCkIMaGaKyJsPq1GMht2QiWawpj95YU4G79z47e2vX7sOPHCJUoDAHaW6pphlL93p75drS9LSlmp7My9V9s93OAmlOGmvSosOEmRKO6KJFHpTKIKD21n83qUbabTMRAVVSShFQEfz17Tn7ZsE09rf6bglUFwx/+bXx9FNx93hQcYNQY1ZEdQU4ONfJZ+b2PHf8fsT03rvBHUEHP3aaR49FVOz2sXecBg+I0LpkTHlj7/yh++ba/4fUhLs7O1+dn3jr9d8++EhGirl33oZm7nWEQ0Wyq9dvdW//s3BhJ7tnrNWefu2V7cvLcXKqOX9YTgzXnj85++Yb1nBlEYeaNaza/+GZyowNs/MX09IVO/3yzupK89UX3TF6pDU6O7t5qTNx/Jmk0Nwdmof51q7Ww2MzrcbEg6G41wf9rbNf7Dn6eAzJJB87eaq6eEUgeZWUqvBapBqiYsgjS903dbtzqTm+f6x9xBGFaB57YuvTz6vehuUhKo0hlt2NxkbvTpDehR8mn33yjy+/Tj8vLh98yFmODsL2wQMjDzS7lxcnT5wCa7K2v7//7qcD84tTM+svvFTeWB/c/HP7+tVyczNZTSZ6ffOTj6+9f8Y5kJIpwBQFYQqaV0SAFmpJ1YBAukgBryFO5JLo0dyDwkWEJiJAqFMVs0iUwsJJKMRFhLX8B0U8eN3MqstXAAAAAElFTkSuQmCC">天弘基金管理有限公司 | 稳健理财，值得信赖！</A>
            <DT><A HREF="https://e.efunds.com.cn/" ADD_DATE="1528880058" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAA20lEQVQ4jbWSMW4CMRBF3zjUEJq0HAGtXaZJATXcI3eACRXdFrkAN2BzkAUOQZNqRZGkCqYwclgJbZZY+dIU39LMPH2PcCn7Mkf8I++HCQ/dD1rI1JyXAhizz78QkTb1M8BqjjmuKFVw6ilVgOI2gj9Iai5bDDHHXaT4likAd744E10hsPqKW/bSCazmCE+UmsUMnK6BadOAf86ghQKB1SqVJGTgdAsQtztd49Q30Rjs7Dll7+93sJu/YbVCuL9OkKhAYLVio/34esMddABqzZmOgM9g/ABP43eeAFBbUFqIDf6HAAAAAElFTkSuQmCC">登录 - 易方达基金网上交易</A>
            <DT><A HREF="http://www.fullgoal.com.cn/" ADD_DATE="1528880442" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAADN0lEQVQ4jVWTbWiVdRjGf/f/eTnn7JzOXppsRqJFzTkqM6kohMCC3mBui7NMbHNOZlqUURBEL6L0hh/6oMsJy6VhkBNtTUom2Ci/REQoFSVijGAuXHOd7TznnOc8z//ugw3s+nR9+cEF13UJ1yt3NFUVl9eK1W5gDfAVaBXIWmBc0UNBjf2GT3pKC4izYNK5oUavEu8WZSewBMgi+quKfCfIjcADguT8kqlPrGj/KfztRAHAAKRbP2vQirNPkF4RPWaM7QB+REWClZc+LpSvtir2CUS/QHlOVfdmcgcXXUvQd8DzA/dtgQ0qvFNwU2+F4fyU73jrQQqJqTo3aVLB/Ej3L5XbHz+dMC6o9GKNU2l8cdyk/0o+BNoFcjSIih8y3FnMuKmlKDcpxAptsdH9ybahZYxuDeYD2YNwHNiUyU48aDBsALBiDzC6Nci2fnqbQr9Vk2lI50/W+YVRa82dDs5AsuPIUsa6CkZlAHAR84yk2w5dAJksBDyZzDj1jo0HrZo7bq2+8ua5La/cpTHh8sF9Fy/P3bDLGP3BRtqXNlE+MN4pgRoDsghhgrFnA9faXlVZU5Ms7Tzf93KLjezzqH3p974XlmX8cLfCw+LJpul7/iwIOgE0GkBRMQAqGgCEFVNXCv1ZEcoIpWKUmK2oUwsgaPG6CVhJtx/+WZS8XzaPhZkwoRV3r6o8mvXDd//Yvs2vWCe6pX/AKcbmNREdcbxwhwQpjbx4DMQ1ahlXWFFOcO/88OYrePEOET2dD/3XF/cPTC7pH5j9Dz4pwqv54S0zkRvfBzQBZxy3pe2qQLvAzVXNrafmjvdMey0dZ0FXWOsstqpNImAj3Rx82T2VzQ3WqXU+ALKKfcOJ1t896U3VVqHSY8Vk0s2t38+d6J72mjrPCtFlhNUgcVD552D18o3ZCNklKk+B7AlGuo45jI9runndecU0AL0Ws8pv6Zhx/eLEfH3lgl9w14HUem7qbzX2PUE6VHQoGZr3ixdXlmXhTDVtQzWhuttFdBtQDVxC9DAqq4GcQllgBpWPEqHsn/l6Y/5aK/+/s1NVLq0SR59GzSOofqvgiHA/cEaNfB44iXMMd8YLyL+2s3CZN78d+wAAAABJRU5ErkJggg==">富国基金管理有限公司</A>
            <DT><A HREF="https://eniu.com/gu/sh601398/roe" ADD_DATE="1593493981" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAACzUlEQVQ4jW2TPWidZRiGr/v9zneSnDa1bZomhmiHqFQomSqK4iCKgw5qJZNDQXQsiLPDQVARB6EudWhR0+qgBF0MlJYUTCUEWoUiUu1fkiYnmlQlzTnJ+fK97+1wQnHwggfu4eHihodHgADvqDLaLHgImPAVRtjFkySGgZxAA7isA1wG6tUqPxUF3wKBsbGxzCYAL/TvprjyFRO+waob2A3sZewl7Hlat2e5OHoQAy/aZPU6VbHN9AkODw7w48hIyFMZ0K4YyYwSBmSyTL3QXI/l2h1eH3qMcQCl1Ze+9tavrbD621O0NVI2XbigohpSDcJOUAU7QiqJWQ85YiPF8HZwWpd9ybQ/gZufUSyR8n2HpcEjinMn7fZ1skEgVNHuN0VlDa+MW0L0DkP/pwRuPfchf3xZuEKs9A3rn4Ev/MHpITYOnCK7v6ZkxP73tNj+yB9//ozjjpchkWitRP958mYg/D1NXlRsFPq71bjT0tTZCy6zXikPOIKq/dyaW9bU+YsuYxcI010ErU1MZvW3GCPnWZVE4l/aU7vKwUODPFg7TihvK2SC5jQD/TUfevhnDfdOIiUTECEr5Bu8Q413aRKBDIBu5M3t87gzEtANtLHB6kKY2UBOg4QAIbAqpBaWMeQo3IeyzE7gTZIJEiQyYItrFUoukdhAdCFZsZS6HnHaeSyo52lT2UcqFsXmeYe7x0W5bCSBRc6FTssFvvGK7N9pe+n55HIleZt0L9kuriUvjJZeIHpec27Q3xEs8agXWfN8n8v2QpFsnx4/lWZnZ5JT9LlzZ9Pk99+lmOzYmim82m0v8BpAsJGGfJV1jtL3aiurDucipb19g3Fzs0gopBgd9+wdiEEQeh7P4cj7eoAzdj10GtQ7wa2ZJ+ytadvR/0u67nLjKDizufdH2xI6Ev9StctXymLjREpbU3b5Q4ztM2XRfMO+u/+/uwD/AkzQsvFiJMOaAAAAAElFTkSuQmCC">工商银行(601398)历史ROE——亿牛网</A>
            <DT><A HREF="https://www.touzid.com/indice/index.html#/" ADD_DATE="1594710062" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAACM0lEQVQ4jX2TTU9TQRiFn5k7c78ALxartqjogpX/zpioEZNrxGji0r/mgpiIQQRqAKWlvV8zd8YFLRQaPavJeb9mznlHsIA8TRKzFpfRaqAJAVpDUyX1WVnqU8iL+Wwxf07Y7ofa3VfIwAlRSUQDDQ6pZSATa61rjDoq2Tq42UBk8Ycnzpp7XjZnqlFHZzCC3M3iHfIVE9kebdiRSv8aVq++A14ApOT9WMmNwjaDCrU3V7iAhO2HiXIPKuv2CvJDAXmcafm0NaIY82YH8PAii0luR3EgoKat1GQMJ7PGt3i3KXSbDQ1fZAfTVchgTHtwUQy3SLqRlmsS24ISgebRCsEmIAFGtAceKTqYrvRhmlXClZCfXwoTBd4ZNflTvf0xrPLdoWFHaJFlvMymThVOqIkPo1XpPKEUoplNBwhRQoc2mLN2LHF1Q5DOGCNGjfMyUv8SaxFu3nLqerJfEw+UFDStl3o+2GC9a1R7xTxfcsgoZLkoL7nPNVAr0RRDqXUP8mXIxwC+boXUbZqavO8TFYTWdlvjzsfUw5v3kr/RxwLcCmF/Ro6oTivDSEXBknZVbEwxGMPXmY0peR8+ZjDdxItFCjdKO/lZ8n7/f0okvF6PVfS4seffJnwaXFtl37Z3kdVpVKuj4+lzrpCnGbbnddxF2pNRzS7k15VN2F4Pte0pLYW3FFa4GkD5MJTKpcZAYzgq2TpkartgAXkax/5OUgWZ0y7SXHznMvZnVZUdw7NyPvsvR/EITp1o0CEAAAAASUVORK5CYII=">最新指数数据-指数估值分析-投资数据网</A>
            <DT><A HREF="http://www.pbc.gov.cn/diaochatongjisi/" ADD_DATE="1602318195">中国人民银行</A>
            <DT><A HREF="https://data.stats.gov.cn/easyquery.htm?cn=A01" ADD_DATE="1602318751">国家数据</A>
            <DT><A HREF="http://data.eastmoney.com/center/macro.html" ADD_DATE="1602318968" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAACqElEQVQ4jX2TTWhcVRTHf+ec+2Ym046ZTmzUhUiwWC24UiiijfEDVNwklixEpIgLixtb6KYoInTVlVAXoisXokWlimJXDa1b8QvEVBCxUoTp1GkSJ3lvMu/de1y0U0LFntU595xz7x/u7y/cJBwUcOawlQ573Wl6xcVbv+LX8YzesCAOenaOACCQBPzylB6r3O6p1F5ImS505+358bxsSfxGBd1F7q9jb44SjznxWcG+VvHX3fW1lKq52z+nN37Jf9lD7a5d7CiU+5LqA0HliSrxaLslzb/X08EU2T3VZKqfpwJhp5q+BOl4AOgu6OGJIK8W7tOgt7TMKR06mdAb+MfZWjpJW38cVjhmUd1LR54Gjqs/xISoHK2Z7HKXVnKvigh1FfrD9O7FC/FAnLSPWpnObJSsi8eVhLTFufu3Z6iHK20ywT2viJlizUDII78PqupQPmR5ZsaW6sY+d6LCWY9sn2ww8U/pzQ7UtfMnQ0HKiSCWkpxfL/3IaBgfNtc7W037oWHs26jYdHeLGk8ksfmaiQtSxIIUWKaUe3mjiHT/uFAtPfg9ZW+/fbOjIbP9TWdQ+XC6ro3uML1HYnVbjcWN0nHo7jxHHgScU/GD8df1FnikEZjtDT06HtuZNlZG/t0dlo701c4AFlSg8mWBpAC+iDkYQBjwc1H5X0GEVpBaHtP5fBCfuhz1WCtjbxEpHRc8nrtOonxKFIgO2jnDGs7JThPLI99WG+nx2nZmJ+tyaK2kzIRsvfRVj5z+D8pco1FS+vBKkd5nFJ+cPk3XsHkTIu7ltkwEkc9u+5JLb4GGrdtjnKe/4CdIr4wx7zlLVZIDKmR56aNUxhM3M+F1Y3HVXPIJ2KXn7JS/GLy7X9/Z0if83wVjNXK1jKub8eW+mTQ8vb3lnH8BV3pF5J9c4ZcAAAAASUVORK5CYII=">经济数据 _ 数据中心 _ 东方财富网</A>
            <DT><A HREF="https://robo.datayes.com/" ADD_DATE="1603431418" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAAAiUlEQVQ4jWO0LT/OQApgIkk1AwMDC4Q61GGBLGpXcQJNBCLIwMDACHfSoQ4LiBAcwEWQpUh2Ej4NcFORbWYhaOTBkAwIw37NDAY0PyCbDVeHDOzXzEBxkl3FCbjtEPMwAROm8cjmIWuDsPH5ARKaaFYxwR2DXye6BlzGY4qzoCnCYw8EMNI8tQIARt03nI8/WLgAAAAASUVORK5CYII=">萝卜投研-智能股票投研|选股_基本面分析|选股|研究|投研_看研报</A>
            <DT><A HREF="https://www.lixinger.com/analytics/index/sh/000905/905/detail/value" ADD_DATE="1603431534" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAACbUlEQVQ4jX3PzUuUURTH8e+9d+aZedQpRS1pKioNLCroTbMWSkg7ISTCXgiKaNGqaNn/UFS0atEmi2hTQdKmNIpaaEiUZcwm1LAsXwrTmefOvaeFjo0Z/bbn8Dm/o+ovdj/etKGmKYrsRNbmJ5TSGYV6hfbPbMSnnvPbp/hPFIdujW7cmK7ZXp9mZjbHTNZijC7MewS5IS725Mm5rV//BWgS8WxmcIT+wRFSZUlKk3Gc84V5i0J1auMeHLj6pu2fgAri3wgDMgND9A0Mk0qFlIRBMQLQKEoetl57c73p0stwEaBFMiRiUJok826I3ndDpEqTlCTjOC9//Stny+IlXS2X+8v/AJpenIcwgFRI5v0wrweGCMOAMIghshgBWgKj7rRcHygDMMsaj+Vy1p9GvCaIgdaMf5kkjyK9shwRwTmPUqq4Sp3x3uw8ub/bpBrapyMfa/R5twGA+DwyNoUDVlUvRwScX4Lszc1UPzUzvfei0j1HdRT5g2gFImA0aMX42M85ZEU5INi8K0aUgrwBSDQeHsGrZmf9avT8gjGgFOPffmCBtasqQBSRzaP1ApI0AFHv3dlU04mxnM13gCgKV4wGDROjk+QE1q+uQsQTRW4BMQUq23f7Y3z3kQrv/B6Kf40ZUJrJz+PMCtSuqUK8kJtr8tVQFL/l1HNj3C7xrnYBESAoIN+ZFcW6dCXgsdbfV/ydY13LML9uolQ7AhQ2jIashV9Z6jatYXNdzU9n7T6zBHjbmWNb2yMdCyyeZkTU4iaKibGp6URZ8viLCw3PlzYoSsmZhzustSfzQquIVKLIGqO73HR0hbsdHwB+A0IODKrP8qBDAAAAAElFTkSuQmCC">理性仁</A>
            <DT><A HREF="http://www.iwencai.com/unifiedwap/home/index" ADD_DATE="1603431614" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAACnklEQVQ4jXWTS2idVRSFv3X+/6b3kaStbYjWgSI4Kig6cCQI4gNHEaWg7RUdqDgKdJCqsztwYImoM0FaoRARqTahIE6kaJVCEaEKPihIhKY2sY/ENjf33v9xloP/pjaCe7rPPmvttfZSoz1/XiG519K3vX7+Mp8+c77RXnhXtcZB5/0+OBUIwGCqShx0Jg7KV1IrnMblBY2MP9qIN4739u17UC5+leJXBA9kp9wsOULErinUHg+1+IE2W/UD829KoejNTb3Dv0j/W432ie9QeCBttBc+s7nS//jp16qWtf7+PZPQpZXL3cwVSM0aPfTXZVBZrRNyTJGCn0yki9AJi/N/jN+1vvsIcXWKwgGgFcEGGXx01ykaz7e1/5OVRE5KixR0XSo3oBPvvjzxBDvWnmU9/R68SPQ2jGXnOJ1kZPUx/v5yP/BeEmKIMVEqSAQJAL1rLRouKZpv6dW1kzCkj+xjjzxE7/QZemtjAI5RkJAC2KpEK0JJVgSyjbo7BFDgZ8xeTHa9SU4gp6ykCkYQtkhbArkgK3N1iMNhqUPEtYwcyIZvQ4UZAKQh1UGskdm4ud2HGNNxSnUo3NnTpLu2k8KRkhqAYnVcW1eo3/E7veXAYP0I42HWs3vewNH0Vg5z7c/baKSB+u2/wDIOMh4yKElKAM1c+AYmX4LwNVnczY2Vw/QvHaVgQEhOkO04qB8ufQ5QxBBtvIWBkfQ6x/z2nefoXTxHLd9FPnqKib0vavrsElxhGAssFbiSIiJvnq7dIVDfvgrbFvHOD3nuo6c0fXbJECpnbhrbFE7VfGH+qh2WenNT999qiGfva2nmxw2q36XNfByYG2+E1hcaGXvYg/WTqa3fcFz+b1g081N3k65uDVe3FTyqCbKNBQqm/wFdpUWJ/wKmDwAAAABJRU5ErkJggg==">同花顺问财</A>
            <DT><A HREF="https://www.hsi.com.hk/schi/indexes/all-indexes/hsi" ADD_DATE="1608171719" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAACz0lEQVQ4jZ2TS2ucZRSAn/e835d0JpNkksylk3QuaTq0xEttlRYtItHYRevWtQiKdFE3uvA/dCFC/4GgC1dCvYSCGBXENAsRzaWKJWnmnk4yzVyS+b73fV0EpaR049kdzuHAOed5FEfCgVcfTefE92a1741ilbX7Qd2Ewe+pTr2uwD3arx5NGonJ0zIcf1dnp67K8XQWLYOgcPv7bVOurLvS1uf9sPtZplptPDageTx/ReXyN7zzZ2fpB9hWC4IAtAatkWQC1+2ZcGl5we42P0xUNlYBBKCZyl2SYvGm//JLs2Zllf5X3yLxUSLXr3Hsnbdx1Rr9W9/gdlvaf23uih4f/6SRyGcAZCdeiJNMfOQ9f246+OEnzF9/o5ITqHgcolFUNIJKJVGRCOHSHezmJt7FC/MSHXzPgRKjw1f1mTOv2FIZu1UCESLXrxH54H1kZAQp5Ind/Bh/fg4chL/+BsciSrIn3qyPpqeFoaHXJZUYNnf/BBFQClup0f96Adfp4BrbBIs/4nq9wx8FAXZjA31iatob8F4QGYnm0BrX7oA6vKnr9bC1Om63hS1XMGt34aB/WFcKu/0AIpFBPH9SjnKA1khiAuX7uF4XlUrinX8OfbLwODGA2IfdTYyB2BBYi4rF0KeLqLExDr68Rbi0jD41gxTyhys6h0xMQLd7QBiUhf3ObVut7XnFU2AMMpXBv/Qi/vwcZnUd88cKujiD9/RTqOEY+B5ysoApVe6F/XDZ033vO7O2vjhwef4NyWbxnn0GPJ/w51+wlSqhtYQra0gmgy4UwNPQ7Tl7f+uLVKt2T/0LkirOfOpfvDBtNu/jdnaw9QbuQROUQiYzqPExJJ1GDccIv1+8HdaabyW3NypHUM7d8M6dnSUMMVsl3MM9EEHGx5BcFrfXNuGd5QW7u/Mfyk+QafKqpNNZBgYGUeDanbYpl9ddufxkmf6vzv8AUk5DUBg4vJYAAAAASUVORK5CYII=">Hang Seng Indexes</A>
        </DL><p>
                ''', 'html5lib')
        dl = soup.html.body.dl
        titles, bookmarks = get_dl_tree(dl)
        self.assertEqual(len(titles), 0)
        self.assertEqual(len(bookmarks), 17)

    def test_dl_multi_level_parent(self):
        soup = BeautifulSoup('''
            <DL><p>
                <DT><H3 ADD_DATE="1616103755" LAST_MODIFIED="1703918961" PERSONAL_TOOLBAR_FOLDER="true">书签栏</H3>
                <DL><p>
                    <DT><H3 ADD_DATE="1616134925" LAST_MODIFIED="1694165629">IT</H3>
                    <DL><p>
                        <DT><H3 ADD_DATE="1616134925" LAST_MODIFIED="1617778561">mac</H3>
                        <DL><p>
                            <DT><A HREF="http://xclient.info/?_=88ceee32f297f9c9aae70169c737c8f4" ADD_DATE="1513055155" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAACb0lEQVQ4jV2SO0wUURiFz38fM7MsLBBkfcGugkQkBFEMxpiojSQktBYmxkoLG2ujJpZGaWyNgUqNDYWxMqFR4yMmNBQSFEwEfEF87LDOzuPe+1uMWni6c8rvO3T42DiISAjkYWZ2AMD4f3cOgGLApbHNEiICQEJIvwg4kOAssWkCAhgk852VTePy4fG2viETNaTv1deWPz+dUU0tJgqbK/u2H52wqSUtTT1cm70Lx4oE1VcX95y6qJt9NoCAicIvzx8WypW9Z680V7pdChngzZ0bNo5UoSi7ewca66ubK4sd+0/YxLKj9v5D4dJ8deJ8e/9Q+qMhff1+Zmpt9p4uthI72VXplUHTr49LYNoyPGpjK72gc+RkcUePbRiv5G/MPVueuaWbSkRgQO6s7iFA6ODn27lCeXepp9fGRmqPjVWBrn/6sDB1lZiFlMwMQOTEiCC9YOnBZG15UfqSTUZKmLi+OH3N/qqR9pgdwCD6ixkEMJEiEmAwQFq8vTcZsVZtWzlLQAQQmAUAImJ2Lsv6zlwq9fSZRua16JVH098+LAXD41QZycWBCIDIbWVRWJ04Vz54JK0lXslbf/1k9eVjf2jMRZtiS0XsGuEs+aMeQqbh986Rse6x00ktUU1+/ePKu/s3RaEZ2gM7pLHsGqRyL9IGA3Lbtq7WvgODF64LJaSvTBy9uX05/v5VJCEzROcuEEFI6qhy+JUboSKl2wdGfyy8MFGqCvrLq9n6yoIutrI1bnUeSlPQAmsgNbXt4M0NGj0+7tLEGUOCOD+ZF4A5xw1rCMgLSclCKjBLz5d+IT80wOxcDoSIIHz6Rx1MzL8BaYIrr83DEgcAAAAASUVORK5CYII=">精品MAC应用分享</A>
                        </DL><p>
                        <DT><H3 ADD_DATE="1616134925" LAST_MODIFIED="1616134925">linux</H3>
                        <DL><p>
                            <DT><A HREF="http://linux.chinaitlab.com/special/linuxcom/" ADD_DATE="1338189417" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAC6ElEQVQ4jTWTzWucZRTFf/e+zzsf6WQyaTKTxmakJFYbGwwNQaj1AxFtQQQpBBGR4spNl936Dwh1Jbiwi4KuXCTqwoVo7ELEqoiCrbWRBGwjSTMz7aSTZt6P57kupp7tgXMOnHMky3NTMUAwAMtpJ23We9fZTboYnkpcZboyy3h5kkgdABgghlMBUCDQ6m+zenuF37s/kuYPCBIA0BDhXJmnhhd4qXmWiXITERBAvM8NjFu9DT5Zu8hOtoWYQ80TRAdWIkTB8ALVuMobR88zW1nAxFBD6PRbfLp2kZ20TRQUNY9XAI8xEEnVEKCX9Pjs5kf8u7+BAGoWuLL1Ofd8h4PxCF7AxIEpQoRYznhhkufrr3KmucR841l6ocs3t1fwwePupi1+a1/lnSMXmBg5wuU/3+fW/k0ER7UwzumpJYoUSC3lxNgzRBJRi0f5/s5XbCebuM3eGrv5XTq+w0jWIA0ZJo7jI4u8/ug5vtv8kh86XyMGqaWcmjjDzNAsq2GZ9e4N3L2kjaKs/HOJoh5gL+xy9MAcbz12ntb+Nj+3rxCZYCJkeQJm9EIXUO5nHdyJ+gscqy2Qh4TLf31AMM/SzLuUtcwvO6vkpJgKZS1xrDZPRs5Pd1YHFRq4SlxlOK6S+BRcYH70FOOlQ2Q+5++9a0SmiMa81nybWnGcLzYusf7gBviI4dIITkQxC0SiRFJkcewkQaCdbdFPEh6vzfF0/TRZ2OfDa++x1d/EEIquwHTlSZwMwiACVVelXmoSPdzqYuM5tvrbLG98TC+7T4g8agIqHK/N0yhN8XDYA4wW61QKVcSU661f+XZzGQQCYM4ThRivGbW4zitTb6KiuAE9ONLh0jQiEDAS28OroSYIAXxMkIyxeJJzT1xgotwE8bj/f+jEcfLwaQTFEGqFBoKSa8D5mKG4wNzoi7z8yFnGSg1UBXCID8HEAqCDLBZAlG7W4o+dq2T0qZUO0RyaYbRwEJUI04hIBID/AHLKPRR214PVAAAAAElFTkSuQmCC">Linux常用命令全集</A>
                            <DT><A HREF="http://www.blogjava.net/DreamAngel/archive/2009/08/09/290408.html" ADD_DATE="1502333722">ubuntu下gcc的安装与使用 - DreamAngel - BlogJava</A>
                            <DT><A HREF="http://vbird.dic.ksu.edu.tw/linux_basic/linux_basic.php" ADD_DATE="1368579926" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAC/0lEQVQ4jVWRS2hcZRiGn//cJjOZySTTJpPb5DKTSQ0hoKYhCkWjtJSAqBSkG90IghewC1FwUTcBBaEIIm7UjSs3LlRwUURqdeGl4iUE7WRsSWJmMuakmds5k5Nz5nwuNDTzwLd54X0W38vqWlFevfyumKkHZTi/LCcnzsrk3BOyU7HlCNvel+ULL8vnX16Xlbc/Er13UYanlyWdOy9GacdmOpchDEOUpgiCNv0nekkmE9TqTVotj/RAiveuvIauaXz/4yqapnGEdu3bG2RGBolGIyDgHfrkshm6IhbPvrjC7OJFzj7+EpZpMD42hOO2OgU/3FgjkYiR6ksStAMkDMnnMogITcfF83y+vv4TH378GSKCACJyV1AobhKGIZnRNL7fRtM0ZqYnADB0HVPXScS7sfeqACg60crlXe7s1zk1NY7b8ojHY+SyIyilUEqBpnDdFuOZIZRSiMh/+ZGg7fls/l1hOj+Gd+Ax0N9HLBrFcVqEoVDdq/LAwhwXL5zDcVqYlolIeFeAplgvbnIqP44c+uQmR6nXm5QrNlfevMQ3Vz/gqy/e55NPr3Ltu5/pTSYIw2MCI2JRvLXF4EAKZehkJ0YoVWxc94DhoX5yk6OE7TZPPrbE/L0zOI7buUJ3rIvbGyUS8RjJVA/ZyRFuFjbQdY3nL73FPaef4v4zz/Dn+gaD6RO4La/zB5GIxa5dxXU9prIZ0v0p1v/awjQMfD8gDEO2y7u88vo7BEGAZZqdM5qGQaPpUN6xWTw9S7QrQvHWFpGIBUqhUCQS3TSaLvZeDcsyONbHUAokFP4o3GbpzDx+u025sodpGigFmq6hFCil6OqyANB1DU1TiCi0UATd0Pl9rcijDy9wZ79GtVrHMHQcp0Wj4VIq7zI3O0WyJ06t1uSg4dL4/wwJBcs0KRQ3SfX1UC7b+H4AwPx9Mxx4h0yMDbFy+QWUUkzlMjy0tECyJ04QBJDOnZeTE+dkOL8s26WKPP3cG9I7+ohsl/6R4/y6WpBffrvZkR16h/IvcltzoD/JjQcAAAAASUVORK5CYII=">鸟哥的 Linux 私房菜 -- 浅谈备份策略</A>
                        </DL><p>
                        <DT><A HREF="https://sms-activate.org/getNumber" ADD_DATE="1679821647">Get a virtual phone number. Temporary number. SMS service activation</A>
                    </DL><p>
                </DL><p>
                <DT><A HREF="https://logdown.com/account/posts/773107-hello-world/edit" ADD_DATE="1468217260" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAABz0lEQVQ4jZWTv2tTURiGn+/ctI3SQkAFp3B/ZHBwKESiVwy9BR0EhwyiOLUQNyfB0cGC/4GLo4uUgOCgBQexHQJZGgi4ONx7e7goLoKBtoYWOceh95YSU4zv+J33fc4L3znSaDTOSam0jrU3AWE6Wazt7O3urpTEcd5gbTRlsJAgcn9+YWFUApby4frvw8OH/X7/10lnEASXReQ8EMdx/HUxiiqzBwcbAtcRWVVFbQXt8bDnea+stZ+NMZvGmJ1arRYNtraGDtwrmqjC3Ov1RgBRFJVc173o+/4NEVnJj28B2hizlHu/FbljQKEsyxaVUt+BK/lIG2N+ADWgP+7/C2CMiYE94FE+KiulNoG1NE3f/xOgtR4Cy8AQwFo7MMYsp2n6bNw7EQCQpuk2EOeANa31YJJvIsDzvCe+738BWsDQdd3t08ITASLSBhygDFSyLHvpum5laoAx5oGIdETkNvAaaCuldnzffxsEwfNTAc1m8wKA1nqQJMnTJEk+VKvV1RxSAVrW2nmAMAzPHDe+GoaGo9f4acZx7na73Z/jt7iuewkoa60H9Xr97MzsbMfCHQC5FoYv7NHOp/2JJ/VRlefmHgts/GfQWng32t9v/QHLU6cFCni8ZgAAAABJRU5ErkJggg==">Logdown</A>
                <DT><A HREF="https://etax.beijing.chinatax.gov.cn/xxmh/html/index_login.html" ADD_DATE="1567317958" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAACxUlEQVQ4jXWSO4icZRSGn/d837//XPaSybqXqGTZgInigkFQtLORiFiIIiwkwSqIRBZEmxhLEyubCBauIjZiGTCFiI2ggsYiimbRIIlGLDYZs+vsZua/fcdiBCtPc5rzvBx4XoFr9TXOKHAiJabE/4//u80YeMP6x2c5rdXX/WyWc6ouQAKz/4AmgWkMukMwSMlxFzGHquDNKLHW1CQZjEpUlOPjqobeNNraxfMJ1G7hm1sw2ZbaOampQWItysgkVDewOIvunnfmeuLAPufCV4ljx4M+v1jzxaWgF58R32zgv/yGOi1IkEUzkhm6NcBPPpu4fzmxdybw/vkRV65V9G+1OPIwrCw7y3eKr78v5SlPIQTDSSZDDvT2wEef1XzwScHOEA4fijyyEuhNi4XZyAP3GCDumjNGo0KQUESmADGDrR3n+acyXjnWodOChdmM24Wxf5/xxnu7PP3qDsMicWgpUFSQ6gpIRDNwwcy0+PJSxY8/1xx9MufltzYBY753B889nnNwqWFpMXB9syYEIUFV15hsrKdK0OkYVeNs78KBhT+Yn7rBhxca+tuJtdU2v/7Z8O75kt60SBpz0Wzsvqqch+4z+jeN3ZHYP3uF727OsX37Xi5fLelNGRcvNzz2YGTjuigqkUWNP5BBzERZO6NSOLA4/TsT8W8OHzQeXclwQCaOP5HR7YjGhRmYAi6BDN87BZNd6LZElVrUzQRZhFEJ7VwcPZIRgqgb8xCETB4lDOHdDvr0W/dyp1aIEySHVsvobzt/DZwbGw0/XXN+uIoPKylvmUuYXnjbdxRoK8FuiYaDgkG/pjfjWDBGhUBO1YjkojsZ6LblFgLgw2iBcxNtTpVDmGw5M5M5vT2BQX9c9k7HUTCCCYtCACblXVGWfk7gOvkOZzxwgoYpd8ei1FSND7crkJAJGUgah0UbuHx9/SU7/Q+uMyM71zN3qgAAAABJRU5ErkJggg==">国家税务总局北京市电子税务局</A>
                <DT><A HREF="https://etax.beijing.chinatax.gov.cn/xxmh/html/index_origin.html?gopage=true&m1=sbjs&m2=aqysb&fromWhere=&qxkzsx=undefined&tabTitle=null&cdId=231&gnDm=gndm-23&toLogin=null#none" ADD_DATE="1570621849" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAACxUlEQVQ4jXWSO4icZRSGn/d837//XPaSybqXqGTZgInigkFQtLORiFiIIiwkwSqIRBZEmxhLEyubCBauIjZiGTCFiI2ggsYiimbRIIlGLDYZs+vsZua/fcdiBCtPc5rzvBx4XoFr9TXOKHAiJabE/4//u80YeMP6x2c5rdXX/WyWc6ouQAKz/4AmgWkMukMwSMlxFzGHquDNKLHW1CQZjEpUlOPjqobeNNraxfMJ1G7hm1sw2ZbaOampQWItysgkVDewOIvunnfmeuLAPufCV4ljx4M+v1jzxaWgF58R32zgv/yGOi1IkEUzkhm6NcBPPpu4fzmxdybw/vkRV65V9G+1OPIwrCw7y3eKr78v5SlPIQTDSSZDDvT2wEef1XzwScHOEA4fijyyEuhNi4XZyAP3GCDumjNGo0KQUESmADGDrR3n+acyXjnWodOChdmM24Wxf5/xxnu7PP3qDsMicWgpUFSQ6gpIRDNwwcy0+PJSxY8/1xx9MufltzYBY753B889nnNwqWFpMXB9syYEIUFV15hsrKdK0OkYVeNs78KBhT+Yn7rBhxca+tuJtdU2v/7Z8O75kt60SBpz0Wzsvqqch+4z+jeN3ZHYP3uF727OsX37Xi5fLelNGRcvNzz2YGTjuigqkUWNP5BBzERZO6NSOLA4/TsT8W8OHzQeXclwQCaOP5HR7YjGhRmYAi6BDN87BZNd6LZElVrUzQRZhFEJ7VwcPZIRgqgb8xCETB4lDOHdDvr0W/dyp1aIEySHVsvobzt/DZwbGw0/XXN+uIoPKylvmUuYXnjbdxRoK8FuiYaDgkG/pjfjWDBGhUBO1YjkojsZ6LblFgLgw2iBcxNtTpVDmGw5M5M5vT2BQX9c9k7HUTCCCYtCACblXVGWfk7gOvkOZzxwgoYpd8ei1FSND7crkJAJGUgah0UbuHx9/SU7/Q+uMyM71zN3qgAAAABJRU5ErkJggg==">国家税务总局北京市电子税务局</A>
            </DL><p>
        ''', 'html5lib')
        dl = soup.html.body.dl
        titles, bookmarks = get_dl_tree(dl)
        self.assertEqual(len(titles), 4)
        # Get first level title
        f_l_titles = []
        for f_l_title in titles:
            if f_l_title['parent_uuid'] == -1:
                f_l_titles.append(f_l_title)
        self.assertEqual(len(f_l_titles), 1)
        # Get second level title
        s_l_titles = []
        for s_l_title in titles:
            if s_l_title['parent_uuid'] == f_l_titles[0]['uuid']:
                s_l_titles.append(s_l_title)
        self.assertEqual(len(s_l_titles), 1)
        self.assertEqual(s_l_titles[0]['title'], 'IT')

        # linux title parent node is IT title
        for sub_title in titles:
            if sub_title['title'] == 'linux':
                self.assertEqual(sub_title['parent_uuid'], s_l_titles[0]['uuid'])

                # Linux常用命令全集's parent is linux title
                for bookmark in bookmarks:
                    if bookmark['title'] == 'Linux常用命令全集':
                        self.assertEqual(bookmark['parent_uuid'], sub_title['uuid'])

        # The number of bookmark is 8
        self.assertEqual(len(bookmarks), 8)
        for bookmark in bookmarks:
            if bookmark['title'] == 'Logdown':
                # The parent_uuid of bookmark is -1
                self.assertEqual(bookmark['parent_uuid'], -1)

if __name__ == '__main__':
    unittest.main()
