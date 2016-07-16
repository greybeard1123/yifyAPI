import argparse
import sys
import time


localtime = time.asctime(time.localtime(time.time()))


class Logger(object):

    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("logfile.log", "a")
        self.log.write("\n\n\n")
        self.log.write("\nNew Log Entry   : " + localtime + "\n")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def logend(self):
        self.log.write("\n\n")
        self.log.write("-" * 48)
        self.log.write("END")
        self.log.write("-" * 49)

    def flush(self):
        pass

sys.stdout = Logger()

parser = argparse.ArgumentParser(description='Read user input')
parser.add_argument(
    "-m", "--min", help="Display minimal details", action="store_true")
parser.add_argument("-q", "--quality",
                    help="Set the movie quality : 720p, 1080p or 3D")
parser.add_argument("-s", "--search", help="Search by movie name. In quotes")
parser.add_argument(
    "-g", "--genre", help="Specify the genre : action, comedy, drama, sci-fi, etc.")
parser.add_argument(
    "-o", "--sort", help="Specify the sort by: title, year, rating, date_added,etc.")
parser.add_argument(
    "-r", "--rotten", help="Display the rotten tomatoes rating : true or false")
parser.add_argument("-l", "--limit", type=int,
                    help="Number of search queries : integer value 1-50")

args = parser.parse_args()

if args.quality == '720p':
    if not args.min:
        print("Quality         : 720p")
elif args.quality == '1080p':
    if not args.min:
        print("Quality         : 1080p")
elif args.quality == '3D':
    if not args.min:
        print("Quality         : 3D")
elif args.quality:
    print("Invalid Movie Quality. Valid: 720p, 1080p, 3D\n")
    sys.exit()

if args.search:
    print("Search for      :", args.search)

if args.genre:
    if not args.min:
        print("Search in genre :", args.genre)

if args.sort == 'title':
    if not args.min:
        print("Sort by         : title")
elif args.sort == 'year':
    if not args.min:
        print("Sort by         : year")
elif args.sort == 'rating':
    if not args.min:
        print("Sort by         : rating")
elif args.sort == 'date_added':
    if not args.min:
        print("Sort by         : date added")
elif args.sort:
    print("Invalid Sort Criteria. Valid: title, year, rating, date_added\n")
    sys.exit()

if args.rotten == 'true':
    if not args.min:
        print("Rotten tomatoes rating included")
elif args.rotten == 'false':
    if not args.min:
        print("Rotten tomatoes rating excluded")
elif args.rotten:
    print("Invalid. vaild: true, false\n")
    sys.exit()

if args.limit is None:
    args.limit = 10
if args.quality is None:
    args.quality = '720p'
if args.search is None:
    args.search = '0'
if args.genre is None:
    args.genre = 'all'
if args.sort is None:
    args.sort = 'date_added'
if args.rotten is None:
    args.rotten = 'false'

if not args.min:
    print("Display ", args.limit, " entries")

quality = args.quality
query_term = args.search
genre = args.genre
sort_by = args.sort
rotten_ratings = args.rotten
limit = str(args.limit)

attr = {'quality': quality, 'query_term': query_term, 'genre': genre,
        'sort_by': sort_by, 'rotten_ratings': rotten_ratings, 'limit': limit}
url = 'https://yts.ag/api/v2/list_movies.json'
