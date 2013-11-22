import os
import sys
import argparse

try:
    import cStringIO as StringIO
except:
    import StringIO
import struct
import json
import csv

def import_data(import_file):
    '''
    Imports data from import_file. 
    Expects to find fixed width row
    Sample row: 161322597 0386544351896 0042
    '''
    mask = '9s14s5s'
    data = []
    with open(import_file, 'r') as f:
        for line in f:
            # unpack line to tuple
            fields = struct.Struct(mask).unpack_from(line)
            # strip any whitespace for each field
            # pack everything in a list and add to full dataset
            data.append(list([f.strip() for f in fields]))
    return data

def write_data(data, export_format):
    '''
    Dispatches call to a specific transformer
    and returns data set.
    Exception is xlsx where we have to save data in a file. 
    '''
    if export_format == 'csv':
        return write_csv(data)
    elif export_format == 'json':
        return write_json(data)
    elif export_format == 'xlsx':
        return write_xlsx(data)
    else:
        raise Exception("Illegal format defined")

def write_csv(data):
    '''
    Transforms data into csv.
    Returns csv as string.
    '''
    # Using this to simulate file IO, 
    # as csv can only write to files.
    f = StringIO.StringIO()
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)
    # Get the content of the file-like object
    return f.getvalue()

def write_json(data):
    '''
    Transforms data into json.
    Very straightforward.
    '''
    j = json.dumps(data)
    return j

def write_xlsx(data):
    '''
    Writes data into xlsx file.
    
    '''
    from xlwt import Workbook
    book = Workbook()
    sheet1 = book.add_sheet("Sheet 1")
    row = 0
    for line in data:
        col = 0
        for datum in line:
            print datum
            sheet1.write(row, col, datum)
            col += 1
        row += 1
        # We have hard limit here of 65535 rows
        # that we are able to save in spreadsheet.
        if row > 65535:
            print >> sys.stderr, "Hit limit of # of rows in one sheet (65535)."
            break
    # XLS is special case where we have to
    # save the file and just return 0
    f = StringIO.StringIO()
    book.save(f)
    return f.getvalue() 
   
   
if __name__ == '__main__':
    # parse input arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("import_file", help="Path to a fixed-width data file.")
    parser.add_argument("export_format", help="Export format: json, csv, xlsx.")
    args = parser.parse_args()

    if args.import_file is None:
        print >> sys.stderr, "You myst specify path to import from."
        sys.exit(1)

    if args.export_format not in ('csv','json','xlsx'):
        print >> sys.stderr, "You must provide valid export file format."
        sys.exit(1)

    # verify given path is accesible file
    if not os.path.isfile(args.import_file):
        print >> sys.stderr, "Given path is not a file: %s" % args.import_file
        sys.exit(1)

    # read from formated fixed-width file
    data = import_data(args.import_file)

    # export data to specified format
    # to make this Unix-lixe pipe-able 
    # we just print to stdout
    print write_data(data, args.export_format)

