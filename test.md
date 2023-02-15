<script
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"
  type="text/javascript">
</script> 

## Generative Art
[Instagram](https://www.instagram.com/openjv92/)

This is an inline equation: $$V_{sphere} = \frac{4}{3}\pi r^3$$,<br>
followed by a display style equation:

$$V_{sphere} = \frac{4}{3}\pi r^3$$


Lets think about some blog posts that I could write for this project. Perhaps one on the form of Bezier functions. Truly, for every new canvas type, there should be an accompanying blog post.

```rust 
pub mod bezier {
    use crate::traits;
    use ndarray::Array;
    use ndarray::IxDyn;

    struct Bezier<A,B> {
        pub control_points: Array<IxDyn, B>,
        pub callparam: fn(Vec<B>) -> Vec<B>,
        pub export_options: A,
    }

    impl<A,B> traits::VectorFunction<B> for Bezier<A, B> {
        fn call(&self, t: Vec<B>) -> Vec<B> {
            todo!();
        }
    }
}

```

```python
from src.typeclass.VFF import VFF

from numpy import array, concatenate, stack

class Bezier(VFF):
    def __init__(self, shape_in: array, shape_out: array, control_points: array, callparam=lambda t:t):
        self.shape_in = shape_in
        self.shape_out = shape_out
        self.control_points = control_points

    @classmethod
    def make_closed(self, _spine: array, _loop: array, _control_points: array):
        pass

    @classmethod
    def make_random(self):
        pass

    @classmethod
    def make_random_closed(self):
        pass

    def __call__(self, t):
        return self.evaluate(t)

    def evaluate(self, t):
        t = self.callparam(t)
        convolve = lambda t, c1, c2: (1-t)*c1 + t*c2
        a = [
                self.shape_in.reshape(self.control_points.shape[0],1),
                self.control_points,
                self.shape_out.reshape(self.control_points.shape[0],1)
            ]
        ## map lambda _: cn over the temp control axis so that below can be a functional
        ## ie return a nested lambda function of t. When moving to multi-dimensional forms
        ## then it'll be lambda t1: lambda t2: ... lambda tn: ?? . Think about this! There's
        ## could be some really interesting shapes here.
        temp_control = concatenate(a, axis=1)
        while temp_control.shape[1] > 1:
            A = [
                    convolve(t, temp_control[:, i], temp_control[:, i+1])
                    for i
                    in range(temp_control.shape[1] - 1)
                ]
            temp_control = stack(A, axis = 1)
        return tuple(temp_control.T.reshape(self.control_points.shape[0]))

    def _evaluate(self, t, arr):
        pass

    ## there may be a problem with this over many splits.
    def split(self, t):
        return [ Bezier(
            self.shape_in, self.shape_out, self.control_points, callparam=lambda nt: t*nt)
               , Bezier(
            self.shape_in, self.shape_out, self.control_points, callparam=lambda nt: (1-t)*nt+t)
               ]
```

```hs
data Tree a = Branch a [Tree a]
            | Leaf a 
            deriving (Show, Foldable)

data BiTree a = Branch' a (BiTree a) (BiTree a)
              | Leaf' a
              deriving (Show, Foldable)

data OrderedBiTree a = Ordered (BiTree a) deriving (Show)

-- We may have to define a merge here.
instance (Monoid a) => Semigroup (BiTree a) where
  tree <> tree' = Branch' mempty tree tree'

instance (Monoid a, Ord a) => Semigroup (OrderedBiTree a) where
  (Ordered tree) <> (Ordered tree') = Ordered $ tree <> tree'

instance (Monoid a) => Monoid (BiTree a) where
  mempty = Leaf' mempty

instance (Monoid a, Ord a) => Monoid (OrderedBiTree a) where
  mempty = (Ordered . Leaf') mempty

instance Functor (Tree) where
  fmap f (Branch x xs) = Branch (f x) (fmap f <$> xs)
  fmap f (Leaf x   )   = Leaf $ f x

instance Functor (BiTree) where
  fmap f (Branch' x l r) = Branch' (f x) (f <$> l) (f <$> r)
  fmap f (Leaf' x    )   = Leaf' $ f x

instance Functor (OrderedBiTree) where
  fmap f (Ordered tree) = Ordered $ fmap f tree
```

[Back to Homepage](/README.md)
