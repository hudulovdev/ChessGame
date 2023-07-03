import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap, QMouseEvent
import chess.svg
import chess

class ChessWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Chess Game")
        self.setGeometry(100, 100, 800, 800)

        self.label = QLabel(self)
        self.label.setGeometry(0, 0, 800, 800)
        
        self.board = chess.Board()
        self.display_chessboard()

    def display_chessboard(self):
        svg = chess.svg.board(board=self.board)
        pixmap = QPixmap()
        pixmap.loadFromData(svg.encode('utf-8'))
        self.label.setPixmap(pixmap)

    def mousePressEvent(self, event: QMouseEvent):
        col = event.x() // 100
        row = 7 - event.y() // 100
        square = chess.square(col, row)

        if self.selected_square is None:
            if self.board.piece_at(square) and self.board.piece_at(square).color == self.board.turn:
                self.selected_square = square
        else:
            move = chess.Move(self.selected_square, square)
            if move in self.board.legal_moves:
                self.board.push(move)
            self.selected_square = None

        self.display_chessboard()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    chess_window = ChessWindow()
    chess_window.show()
    sys.exit(app.exec_())
