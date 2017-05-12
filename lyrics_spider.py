import scrapy
import urlparse

class LyricsSpider(scrapy.Spider):
    name = "lyricswikia"
    singer_list = [
            'Taylor_Swift',
            'EMINEM',
            'RIHANNA',
            'Beyonce',
            'Bruno_Mars',
            'Katy_Perry',
            'Justin_Timberlake',
            'Lady_Gaga',
            'JAY_Z',
            'Selena_Gomez',
            'Ariana_Grande',
            'Drake',
            'Ed_Sheeran',
            'ADELE',
            'Shawn_Mendes',
            'Justin_Bieber',
            'Maroon_5',
            'Cold_Play',
            'The_Chainsmokers',
            'Metallica'
    ]
#    singer_list = [
#
#            'Justin_Timberlake'
#
#    ]
    start_urls = list(map(lambda x: 'http://lyrics.wikia.com/wiki/' + x, singer_list))
    #start_urls = [
    #    'http://lyrics.wikia.com/wiki/Taylor_Swift',
    #    'http://lyrics.wikia.com/wiki/EMINEM'
    #]
    n = 1
    def parse(self, response):
        for songurl in response.xpath('//div[@id="mw-content-text"]/ol/li/b/a/@href').extract():
            if songurl is not None:
                self.log('Read song number %d' % self.n)
                self.n += 1
                nextpage = urlparse.urljoin('http://lyrics.wikia.com', songurl)
                yield scrapy.Request(nextpage, callback=self.parse_lyrics)
            
    def parse_lyrics(self, response):
        lyrics = response.xpath('//div[@class="lyricbox"]/text()').extract()
        songname = response.xpath('//div[@id="song-header-title"]/b/text()').extract_first().lstrip()
        
        singername = response.xpath('//div[@class="header-column header-title"]/h1/text()').extract_first().lstrip()
        singername = singername.split(':', 1)[0]
        filename = 'lyrics/%s.txt' % singername
        with open(filename, 'a') as f:
            f.write(songname)
#            f.write('. ')
            for line in lyrics:
                f.write('. ')
                f.write(line)
                
#            f.write('\n')
        self.log('Saved file %s' % filename)